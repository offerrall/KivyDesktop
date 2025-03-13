# KivyDesktop

A modern, desktop-focused UI component library built on top of Kivy. KivyDesktop simplifies Kivy development by disabling mobile-specific behaviors and providing enhanced UI components with desktop-specific interactions like hover effects and improved styling options.

## Overview

KivyDesktop enhances Kivy for desktop application development by providing:
- Customizable buttons with icon support and alignment options
- Numeric input fields with increment/decrement and drag-to-change functionality
- Scroll views with automatic content layout adjustment and simplified configuration
- Consistent theming and styling across components

## Installation

```bash
pip install kivy-desktop
```

## Requirements
- Python 3.7+
- Kivy 2.0.0+

## Features

### Enhanced Desktop Interactions
- **Mouse hover effects**: All components respond to mouse hover
- **Drag interactions**: Numeric fields support click-and-drag to change values
- **Desktop optimizations**: Configured for desktop use with standard mouse behavior

### Modern UI Components
- **DButton**: Advanced button with hover effects, icon support, and content alignment
- **DNumeric**: Numeric input field with plus/minus buttons and drag interaction
- **DScrollView**: Simplified scrollview with automatic content layout
- **DApp**: Streamlined application startup and configuration

### Customization
- Consistent theming with easy color customization
- Component-specific styling for borders, backgrounds, and text
- Configurable component behavior and appearance

## Usage Examples

### Basic Application

```python
from kivy_desktop.app import DApp
from kivy_desktop.button import DButton
from kivy.uix.boxlayout import BoxLayout

class MyApp:
    def __init__(self):
        # Create main container
        self.container = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add a button
        button = DButton(text="Click Me!", release_callback=self.on_button_press)
        self.container.add_widget(button)
        
        # Create and run the app
        self.app = DApp(self.container, title="My Desktop App")
        self.app.run()
    
    def on_button_press(self, button):
        print("Button pressed!")

if __name__ == "__main__":
    MyApp()
```

### DButton with Icon

```python
from kivy_desktop.button import DButton
from kivy.uix.boxlayout import BoxLayout

layout = BoxLayout(padding=10)

# Create button with icon
button = DButton(
    text="Save",
    icon_source="icons/save.png",
    icon_placement="left",
    content_alignment="center",
    release_callback=lambda btn: print("Save clicked")
)

layout.add_widget(button)
```

### DNumeric Input

```python
from kivy_desktop.numeric import DNumeric
from kivy.uix.boxlayout import BoxLayout

layout = BoxLayout(padding=10)

# Create numeric input
numeric = DNumeric(
    value=50,
    min_value=0,
    max_value=100,
    step=5,
    use_float=False,
    on_change_callback=lambda widget, value: print(f"Value changed to {value}")
)

layout.add_widget(numeric)
```

### DScrollView

```python
from kivy_desktop.scroll import DScrollView
from kivy_desktop.button import DButton
from kivy.uix.boxlayout import BoxLayout

# Create a scroll view
scroll = DScrollView(orientation='vertical', spacing=5, padding=10)

# Add widgets to the scroll view
for i in range(20):
    btn = DButton(text=f"Item {i}", size_hint_y=None, height=40)
    scroll.add_widget(btn)

# Add to your layout
root = BoxLayout()
root.add_widget(scroll)
```

## Component Reference

### DButton

A customizable button with hover effects, icon support, and content alignment options.

**Key properties:**
- `text`: Button label text
- `icon_source`: Path to icon image
- `icon_placement`: Position of icon ('left' or 'right')
- `content_alignment`: Alignment of content ('left', 'center', 'right')
- `release_callback`: Function to call when button is released
- `background_color`: Normal background color
- `background_color_down`: Pressed background color
- `border_color`: Border color
- `border_hover`: Border color when hovered

### DNumeric

A numeric input field with increment/decrement buttons and drag-to-change functionality.

**Key properties:**
- `value`: Current numeric value
- `min_value`: Minimum allowed value
- `max_value`: Maximum allowed value
- `step`: Amount to increment/decrement
- `use_float`: If True, allows floating point values
- `float_precision`: Number of decimal places when using floats
- `on_change_callback`: Function to call when value changes
- `drag_sensitivity`: Controls sensitivity of drag-to-change

### DScrollView

A simplified scroll view with automatic content layout adjustment.

**Key properties:**
- `orientation`: Direction of scrolling ('vertical' or 'horizontal')
- `spacing`: Space between child widgets
- `padding`: Padding inside the scroll view
- `auto_adjust_height`: If True, automatically adjusts height based on content

## Customization

### Theming

You can customize the color theme by modifying the color values in `theme.py`:

```python
from kivy_desktop.theme import COLORS

# Customize colors
COLORS['back1'] = [0.15, 0.15, 0.15, 1]  # Lighter background
COLORS['seleted'] = [0.2, 0.6, 1, 1]     # Blue highlight
```

### Component Styling

Each component has properties for customizing its appearance:

```python
button = DButton(
    background_color=[0.2, 0.2, 0.2, 1],
    border_color=[0.1, 0.1, 0.1, 1],
    font_color=[1, 1, 1, 1],
    background_radius=[10, 10, 10, 10],
    internal_padding=[15, 10, 15, 10]
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Developed with ❤️ for the Kivy community

Built on top of [Kivy](https://kivy.org/), a powerful open-source Python framework for developing multi-touch applications.