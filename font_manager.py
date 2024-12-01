import tkinter.font as tkfont


def configure():   

    # Set the desired font family. You can switch to another font family if needed.
    # Uncomment "Segoe UI" for an alternative.
    # family = "Segoe UI"
    family = "Helvetica"

    # Configure the default font used by most widgets (e.g., labels, buttons)
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family) # Set font size and family
    
    # Configure the font used in text areas (e.g., text widgets)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family) # Set font size and family for text
    
    # Configure the font used for fixed-width (monospace) widgets
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family) # Set font size and family for fixed-width
