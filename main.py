import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 █████╗ ██╗   ██╗████████╗ ██████╗     ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
███████║██║   ██║   ██║   ██║   ██║    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██╔══██║██║   ██║   ██║   ██║   ██║    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗██████╗  █████╗  ██████╗███████╗  
██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝  
██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ███████╗██████╔╝███████║██║     █████╗    
██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝    
╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗███████║██║     ██║  ██║╚██████╗███████╗  
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ 
                                                             (by Juanfu224)
"""

def menu():
    red()
    print(banner)
    yellow()
    time.sleep(0.5)
    print("1 -> Instalar y configurar Kitty, P10k, FZF, Nvim, plugins etc...")
    time.sleep(0.5)
    print("\n2 -> Instalar y configurar Bspwm, Polybar, Picom y Rofi")
    time.sleep(0.5)
    print("\n3 -> Instalar NordVPN")
    time.sleep(0.5)
    print("\n4 -> Instalar VirtualBox")
    time.sleep(0.5)
    print("\n5 -> Instalar LibreOffice")
    time.sleep(0.5)
    print("\n6 -> Instalar Sublime Text")
    time.sleep(0.5)
    print("\n7 -> ALL IN ONE")
    time.sleep(0.5)
    print("\n8 -> Salir")
    time.sleep(0.5)

    option = input("\n-->> ")

    if option == "1":
        p10k()
    if option == "2":
        bspwm()
    if option == "3":
        vpn()
    if option == "4":
        vbox()
    if option == "5":
        office()
    if option == "6":
        sublime()
    if option == "7":
        p10k()
        bspwm()
        vpn()
        vbox()
        office()
        sublime()
    if option == "8":
        exit()

def p10k():
    blue()
    print("\n[+] Instalando y configurando Powerlevel10k, plugins, FZF, Nvim, etc....\n")
    
    # Descargar todo lo necesario
    print("\n[+] Descargando todo lo necesario....\n")
    os.system("sudo apt install zsh zsh-autosuggestions zsh-syntax-highlighting scrub fzf kitty -y")
    os.system("sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/Hack.zip")
    os.system("sudo wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh")
    os.system("sudo wget https://github.com/neovim/neovim/releases/download/stable/nvim.appimage")
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k")
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/powerlevel10k")
    os.system("sudo git clone --depth=1 https://github.com/junegunn/fzf.git ~/.fzf")
    os.system("sudo git clone --depth=1 https://github.com/junegunn/fzf.git /root/.fzf")

    # Instalar Hack Nerd Fonts
    print("\n[+] Instalando las Hack Nerd Fonts....\n")
    os.system("unzip Hack.zip")
    os.system("sudo cp -r Hack*.ttf /usr/share/fonts ")
    os.system("sudo rm -r Hack*")

    #Configurar Kitty
    print("\n[+] Configurando la Kitty....\n")
    os.system("sudo rm -r ~/.config/kitty*")
    os.system("sudo mkdir ~/.config/kitty")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/terminal/kitty.conf ~/.config/kitty")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/terminal/color.ini ~/.config/kitty")

    #Instalar P10k
    print("\n[+] Instalando Powerlevel10k....\n")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/zsh/.zshrc ~/")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/zsh/.zshrc /root")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/zsh/.p10k.zsh ~/")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/zsh/.p10k.zsh /root")

    #Instalar plugins
    print("\n[+] Instalando plugins....\n")
    os.system("sudo dpkg -i ~/Auto-Linux-Workspace/tools/zsh/bat*")
    os.system("sudo dpkg -i ~/Auto-Linux-Workspace/tools/zsh/lsd*")
    os.system("sudo mkdir /usr/share/zsh-sudo")
    os.system("sudo cp -r sudo.plugin.zsh /usr/share/zsh-sudo")
    os.system("sudo rm -r ~/Auto-Linux-Workspace/sudo.plugin*")

    #Instalar FZF en usuario
    print("\n[+] Instalando FZF en usuario....\n")
    os.system("sudo ~/.fzf/install")

    #Instalar FZF en root
    print("\n[+] Instalando FZF en root....\n")
    os.system("sudo /root/.fzf/install")

    #Borrar antigua configuración de Nvim
    print("\n[+] Borrando antigua configuración de Nvim....\n")
    os.system("sudo rm -rf ~/.config/nvim")
    os.system("sudo rm -rf ~/.local/share/nvim")
    os.system("sudo rm -rf ~/.cache/nvim")
    os.system("sudo rm -rf /root/.config/nvim")
    os.system("sudo rm -rf /root/.local/share/nvim")
    os.system("sudo rm -rf /root/.config/nvim")
    
    #Instalar Nvim
    print("\n[+] Aplicando la nueva configuración de Nvim en usuario....\n")
    os.system("sudo chmod 755 nvim.appimage")
    os.system("sudo mv nvim.appimage /bin")
    
    #Configurar Nvim en usuario
    print("\n[+] Aplicando la nueva configuración de Nvim en usuario....\n")
    os.system("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1")
    os.system("nvim.appimage")

    #Configurar Nvim en root
    print("\n[+] Aplicando la nueva configuración de Nvim en root....\n")
    os.system("sudo git clone https://github.com/NvChad/NvChad /root/.config/nvim --depth 1")
    os.system("sudo nvim.appimage")
    
    #Configurar zsh por defecto
    print("\n[+] Configurando zsh por defecto....\n")
    os.system("sudo usermod --shell /usr/bin/zsh $USER")
    os.system("sudo usermod --shell /usr/bin/zsh root")
    
    #Cambiar terminal por defecto
    print("\n[+] Configurando terminal por defecto....\n")
    print("\n[+] Elige que terminal quieres tener por defecto:")
    os.system("sudo update-alternatives --config x-terminal-emulator")
    
    time.sleep(2)
    blue()
    print("\n[+] La instalación y la configuración de la terminal se ha realizado corectamente")
    print("\n[+] Para que funcione correctamente Powerlevel10k es necesario tener las Hack Nerd Fonts puestas en la configuración de la tipografía de la terminal, aún asi, la Kitty ya viene configurada con todo lo necesario.\n")

def bspwm():
    blue()
    print("[+] Instalando requerimientos necesarios para bspwm...\n")

    # Instalando Requerimientos
    os.system("sudo apt update")
    os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
    os.system("sudo apt install bspwm caja feh scrot xclip tmux acpi scrub bat wmname pulseaudio alsa-utils pamix brightnessctl isc-dhcp-server -y")
    os.system("sudo apt -f -y install")
    os.system("sudo apt autoclean")

    time.sleep(2)
    blue()
    print("\n[+] Requetimientos instalados correctamente\n")
    print("\n[+] Instalando y configurando bspwm.....\n")

    # Clona la repo de bspwm
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("mv bspwm/* .")
    os.system("sudo rm -r bspwm/")
    os.system("make")

    # Acaba del build
    os.system("sudo make install")

    # Elimina los archivos de bspwm
    os.system("sudo rm -r artworks/ contrib/ doc/ src/ tests/ bspc bspc.o bspwm bspwm.o desktop.o events.o ewmh.o geometry.o helpers.o history.o jsmn.o LICENSE Makefile messages.o monitor.o parse.o pointer.o query.o README.md restore.o rule.o settings.o Sourcedeps stack.o subscribe.o tree.o VERSION window.o")

    # Clona la repo de sxhkd
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.system("mv sxhkd/* .")
    os.system("sudo rm -r sxhkd/")
    os.system("cd ../sxhkd")
    os.system("make")

    # Acaba el build
    os.system("sudo make install")

    # Crea las carpetas de bspwm y sxhkd en ~/.config
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")
    os.system("cp examples/bspwmrc ~/.config/bspwm/")

    # Les da permisos de ejecucion a bspwmrc
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("cp examples/sxhkdrc ~/.config/sxhkd/")

    # Elimina los archivos de sxhkd
    os.system("sudo rm -r contrib/ doc/ examples/ src/ grab.o helpers.o LICENSE Makefile parse.o README.md Sourcedeps sxhkd sxhkd.o types.o VERSION")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/bspwm/sxhkdrc ~/.config/sxhkd")

    # Clona el repo de polybar
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.system("mv polybar/* .")
    os.system("sudo rm -r polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")

    # Acaba el build
    os.system("sudo make install")

    # Elimina los archivos de polybar
    os.system("sudo rm -r bin/ cmake/ CMakeFiles/ common/ config/ contrib/ doc/ generated-sources/ include/ lib/ libs/ polybar/ src/ tests/ banner.png build.sh CHANGELOG.md CMajeCache.txt cmake_install.cmake CMakeLists.txt compile_commands.json CONTRIBUTING.md install_manifest LICENSE Makefile README.md SUPPORT.md version.txt")

    # Clona el repo de picom
    os.system("git clone https://github.com/ibhagwan/picom.git")
    os.system("mv picom/* .")
    os.system("sudo rm -r picom/")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")

    # Hace el build de picom
    os.system("sudo ninja -C build install")

    # Elimina los archivos de picom
    os.system("sudo rm -r *.md *.conf *.desktop *.txt *.build *.spdx *.glsl COPYING Doxyfile CONTRIBUTORS bin/ build/ dbus-examples/ LICENSES/ man/ media/ meson/ src/ subprojects/ tests/")

    # Añade el wallpaper
    os.system("mkdir ~/.wallpapers")
    os.system("cp ~/Auto-Linux-Workspace/tools/bspwm/wallpaper.jpg ~/.wallpapers")
    os.system("echo 'feh --bg-fill ~/.wallpapers/wallpaper.jpg' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'xsetroot -cursor_name left_ptr &' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'wmname LG3D &' >> ~/.config/bspwm/bspwmrc")

    # Copia el tema de polybar a ~/.config
    os.system("sudo mv ~/Auto-Linux-Workspace/tools/bspwm/polybar-backup.zip .")
    os.system("unzip ~/Auto-Linux-Workspace/polybar-backup.zip")
    os.system("sudo mv ~/Auto-Linux-Workspace/polybar-backup/ ~/.config/")
    os.system("sudo rm -r ~/.config/polybar/ 2>/dev/null")
    os.system("sudo mv ~/.config/polybar-backup/ ~/.config/polybar/")
    os.system("echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc")
    os.system("sudo rm -r ~/Auto-Linux-Workspace/polybar-backup/")

    # Copia la config de picom
    os.system("mkdir ~/.config/picom")
    os.system("echo 'bspc config focus_follows_pointer true' >> ~/.config/bspwm/bspwmrc")
    os.system("cp ~/Auto-Linux-Workspace/tools/bspwm/picom.conf ~/.config/picom")
    os.system("echo 'bspc config border_width 0' >> ~/.config/bspwm/bspwmrc")
    os.system("mkdir ~/.config/bin")
    os.system("echo 'picom --experimental-backends &' >> ~/.config/bspwm/bspwmrc")

    # Instalacion de Fuentes para Polybar
    os.system("sudo cp ~/.config/polybar/fonts/* /usr/share/fonts")

    # Mete el ethernet_status.sh, hackthebox_status.sh, target_to_hack.sh y target en ~/.config/bin
    os.system("chmod +x ~/Auto-Linux-Workspace/tools/bspwm/ethernet_status.sh 2>/dev/null")
    os.system("mv ~/Auto-Linux-Workspace/tools/bspwm/ethernet_status.sh ~/.config/bin")
    os.system("chmod +x ~/Auto-Linux-Workspace/tools/bspwm/hackthebox.sh")
    os.system("mv ~/Auto-Linux-Workspace/tools/bspwm/hackthebox.sh ~/.config/bin")
    os.system("chmod +x ~/Auto-Linux-Workspace/tools/bspwm/target_to_hack.sh")
    os.system("mv ~/Auto-Linux-Workspace/tools/bspwm/target_to_hack.sh ~/.config/bin")
    os.system("echo '' > ~/.config/bin/target")
    os.system("chmod +x ~/Auto-Linux-Workspace/tools/bspwm/battery.sh")
    os.system("mv ~/Auto-Linux-Workspace/tools/bspwm/battery.sh ~/.config/bin/")
    os.system("echo '' > ~/.config/bin/target")

    # Instalar Rofi
    os.system("sudo apt install libxkbcommon-x11-dev librust-pangocairo-sys-dev libstartup-notification0-dev libgdk-pixbuf-2.0-dev check")
    os.system("wget https://github.com/davatorium/rofi/releases/download/1.7.5/rofi-1.7.5.tar.gz")
    os.system("tar -xvzf rofi-1.7.5.tar.gz")
    os.system("sudo mv rofi-1.7.5/* .")
    os.system("./configure")
    os.system("make")
    os.system("sudo make install")

    # Configurar Rofi
    os.system("git clone https://github.com/adi1090x/rofi.git")
    os.system("mv rofi/* .")
    os.system("sudo chmod +x setup.sh")
    os.system("sudo ./setup.sh")
    os.system("sudo rm -rf files fonts previews rofi LICENSE README.md setup.sh")
    os.system("sudo cp -r ~/Auto-Linux-Workspace/tools/bspwm/launcher.sh ~/.config/rofi/launchers/type-1/")
    os.system("sudo chmod +x ~/.config/rofi/launchers/type-1/launcher.sh")

    # Mueve los comandos settarget y cleartarget a /bin
    os.system("sudo cp ~/Auto-Linux-Workspace/tools/bspwm/settarget /bin")
    os.system("sudo cp ~/Auto-Linux-Workspace/tools/bspwm/cleartarget /bin")
    os.system("sudo chmod +x /bin/settarget")
    os.system("sudo chmod +x /bin/cleartarget")

    # Instalando fastTCPscan.go
    os.system("chmod +x ~/Auto-Linux-Workspace/tools/bspwm/fastTCPscan.go")
    os.system("sudo cp ~/Auto-Linux-Workspace/tools/bspwm/fastTCPscan.go /bin")

    # Instalando wichSystem.py
    os.system("sudo chmod +x ~/Auto-Linux-Workspace/tools/bspwm/wichSystem.py")
    os.system("sudo mv ~/Auto-Linux-Workspace/tools/bspwm/wichSystem.py /bin/")

    # Copiamos configuración de Rofi
    os.system("sudo cp ~/Auto-Linux-Workspace/tools/bspwm/powermenu_alt.rasi ~/.config/polybar/scripts/themes/powermenu_alt.rasi")

    time.sleep(2)
    blue()
    print("\n[+] Bspwm se ha instalado y configurado correctamente\n")

def vpn():
    blue()
    print("\nInstalando NordVPN....\n")

# Instalamos NordVPN....
    os.system("sudo dpkg -i ~/Auto-Linux-Workspace/tools/zsh/nordvpn-release_1.0.0_all.deb")
    os.system("sudo apt update")
    os.system("sudo apt install nordvpn")

    time.sleep(2)
    blue()
    print("\n[+] NordVPN se ha instalado correctamente\n")

def vbox():
    blue()
    print("\nInstalando VirtualBox....\n")

# Instalamos VirtualBox....
    os.system("sudo wget https://download.virtualbox.org/virtualbox/7.0.8/virtualbox-7.0_7.0.8-156879~Ubuntu~jammy_amd64.deb")
    os.system("sudo dpkg -i virtualbox*")
    os.system("sudo apt -f -y install")
    os.system("sudo rm -r virtualbox*")
    os.system("sudo adduser $USER vboxusers")
    os.system("sudo adduser $USER vboxsf")

    time.sleep(2)
    blue()
    print("\n[+] VirtualBox instalado correctamente\n")

def office():
    blue()
    print("\nInstalando LibreOffice....\n")

# Instalamos LibreOffice....
    os.system("wget https://download.documentfoundation.org/libreoffice/stable/7.5.1/deb/x86_64/LibreOffice_7.5.1_Linux_x86-64_deb.tar.gz")
    os.system("wget https://download.documentfoundation.org/libreoffice/stable/7.5.1/deb/x86_64/LibreOffice_7.5.1_Linux_x86-64_deb_helppack_es.tar.gz")
    os.system("wget https://download.documentfoundation.org/libreoffice/stable/7.5.1/deb/x86_64/LibreOffice_7.5.1_Linux_x86-64_deb_langpack_es.tar.gz")
    os.system("tar -xvzf ~/Auto-Linux-Workspace/LibreOffice_7.5.1_Linux_x86-64_deb.tar.gz")
    os.system("tar -xvzf ~/Auto-Linux-Workspace/LibreOffice_7.5.1_Linux_x86-64_deb_helppack_es.tar.gz")
    os.system("tar -xvzf ~/Auto-Linux-Workspace/LibreOffice_7.5.1_Linux_x86-64_deb_langpack_es.tar.gz")
    os.system("sudo dpkg -i ~/Auto-Linux-Workspace/LibreOffice_7.5.1.2_Linux_x86-64_deb/DEBS/*")
    os.system("sudo dpkg -i ~/Auto-Linux-Workspace/LibreOffice_7.5.1.2_Linux_x86-64_deb_langpack_es/DEBS/*")
    os.system("sudo dpkg -i ~/Auto-Linux-Workspace/LibreOffice_7.5.1.2_Linux_x86-64_deb_helppack_es/DEBS/*")
    os.system("sudo rm -r ~/Auto-Linux-Workspace/LibreOffice*")
    
    time.sleep(2)
    blue()
    print("\n[+] LibreOffice instalado correctamente\n")

def sublime():
    blue()
    print("\nInstalando Sublime Text....\n")

# Instalamos Sublime-text
    os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null")
    os.system("echo ""deb https://download.sublimetext.com/ apt/stable/"" | sudo tee /etc/apt/sources.list.d/sublime-text.list")
    os.system("sudo apt update")
    os.system("sudo apt install sublime-text -y")


    time.sleep(2)
    blue()
    print("\n[+] Sublime Text instalado correctamente\n")

if __name__ == '__main__':
    menu()
