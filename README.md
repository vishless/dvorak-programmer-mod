This is a modified version of https://github.com/ThePrimeagen/keyboards

# Installation

I couldn't get it to work by copying the layout file to `.config/xkb/`. Below steps worked.

PLEASE MAKE A BACKUP OF THE FILES BEFORE EDITING

Add the new layout to the symbols directory
Open `/usr/share/X11/xkb/symbols/us` and add the symbols from file `real-prog-dvorak-mod` under Dvorak Programmer

Update evdev by opening `/usr/share/X11/xkb/rules/evdev.xml`

And add the following
```
<variant>
    <configItem>
        <name>real-prog-dvorak-mod</name>
        <description>English (Real Programmers Dvorak)</description>
        <vendor>MichaelPaulson</vendor>
    </configItem>
</variant>
```
To permanently set the layout  
Edit `/etc/default/keyboard` and set  
`XKBVARIANT="real-prog-dvorak-mod"`
