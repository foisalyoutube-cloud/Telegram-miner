package com.example.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable

private val DarkColorScheme = darkColorScheme(
    primary = TgAccentBlue,
    secondary = TgAccentGold,
    tertiary = TgAccentGreen,
    background = TgDarkBg,
    surface = TgCardBg,
    onPrimary = TgTextWhite,
    onSecondary = TgDarkBg,
    onTertiary = TgDarkBg,
    onBackground = TgTextWhite,
    onSurface = TgTextWhite
)

@Composable
fun MyApplicationTheme(
    content: @Composable () -> Unit
) {
    MaterialTheme(
        colorScheme = DarkColorScheme,
        typography = Typography,
        content = content
    )
}
