package com.example

import android.annotation.SuppressLint
import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.view.ViewGroup
import android.webkit.WebChromeClient
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.viewinterop.AndroidView
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import com.example.ui.theme.MyApplicationTheme
import java.io.File

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Pre-create WebView Code Cache directories to prevent Chromium simple_file_enumerator opendir errors
        try {
            File(cacheDir, "WebView/Default/HTTP Cache/Code Cache/js").mkdirs()
            File(cacheDir, "WebView/Default/HTTP Cache/Code Cache/wasm").mkdirs()
        } catch (_: Exception) {}

        enableEdgeToEdge()
        setContent {
            MyApplicationTheme {
                TelegramMinerScreen()
            }
        }
    }
}

@SuppressLint("SetJavaScriptEnabled")
@Composable
fun TelegramMinerScreen() {
    var webViewInstance: WebView? = remember { null }
    val lifecycleOwner = LocalLifecycleOwner.current

    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_RESUME -> webViewInstance?.onResume()
                Lifecycle.Event.ON_PAUSE -> webViewInstance?.onPause()
                Lifecycle.Event.ON_DESTROY -> webViewInstance?.destroy()
                else -> {}
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose {
            lifecycleOwner.lifecycle.removeObserver(observer)
        }
    }

    BackHandler(enabled = true) {
        if (webViewInstance?.canGoBack() == true) {
            webViewInstance?.goBack()
        }
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(androidx.compose.ui.graphics.Color(0xFF0E141F))
            .safeDrawingPadding()
            .testTag("telegram_miner_screen")
    ) {
        AndroidView(
            modifier = Modifier
                .fillMaxSize()
                .testTag("telegram_miner_webview"),
            factory = { context ->
                WebView(context).apply {
                    layoutParams = ViewGroup.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT,
                        ViewGroup.LayoutParams.MATCH_PARENT
                    )
                    setBackgroundColor(Color.parseColor("#0E141F"))
                    
                    settings.apply {
                        javaScriptEnabled = true
                        domStorageEnabled = true
                        databaseEnabled = true
                        useWideViewPort = true
                        loadWithOverviewMode = true
                        // Use LOAD_NO_CACHE for local bundled APK assets to prevent corrupted disk cache index reconstruction
                        cacheMode = WebSettings.LOAD_NO_CACHE
                        allowFileAccess = true
                        mediaPlaybackRequiresUserGesture = false
                    }
                    webViewClient = object : WebViewClient() {
                        override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
                            return false
                        }
                    }
                    webChromeClient = WebChromeClient()
                    loadUrl("file:///android_asset/index.html")
                    webViewInstance = this
                }
            },
            update = {
                webViewInstance = it
            }
        )
    }
}
