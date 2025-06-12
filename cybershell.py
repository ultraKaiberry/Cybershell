from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from random import choice
from time import sleep
import os

console = Console()
fig = Figlet(font='slant')
colors = ['bright_magenta', 'cyan', 'bright_green', 'bright_yellow']
log = []
trace_level = 0

def glitch_text(text):
    t = Text()
    for c in text:
        t.append(c, style=choice(colors))
    return t

def draw_banner(word="cyber space"):
    console.print(glitch_text(fig.renderText(word)))

def display_log():
    text = Text()
    for line in log[-10:]:
        text.append(line + '\n', style=choice(colors))
    return Panel(text, border_style=choice(colors), title="[cyan]SYS-LOG")

def typewriter(text, delay=0.01):
    result = Text()
    for char in text:
        result.append(char, style=choice(colors))
        console.print(result, end='\r')
        sleep(delay)
    result = Text()
    console.print(glitch_text(text))

def handle_command(cmd):
    cmd = cmd.strip()

    if cmd == "python":
        os.system("python3") 
    elif cmd.startswith("nmap "):
        os.system("nmap")
        log.append(f">> Executed: {cmd}")
    elif cmd == "msfconsole":
        os.system("msfconsole")
        log.append(">> Launched msfconsole")
    elif cmd.startswith("open "):
        filename = cmd.split(" ", 1)[1]
        try:
            with open(filename, 'r') as f:
                contents = f.read()
            log.append(f">> OPENED FILE: {filename}")
            log.append(contents)
        except FileNotFoundError:
            log.append(f"[red]>> FILE NOT FOUND: {filename}[/red]")
    elif cmd.startswith("write "):
        parts = cmd.split(" ", 2)
        if len(parts) < 3:
            log.append("[red]>> USAGE: write filename content[/red]")
        else:
            filename, content = parts[1], parts[2]
            with open(filename, 'w') as f:
                f.write(content)
            log.append(f">> WROTE TO FILE: {filename}")
    else:
        log.append(">> UNKNOWN COMMAND")

def shell():
    draw_banner()
    while True:
        console.print(display_log())
        console.print("[bold cyan]λ[/bold cyan] ", end="")
        cmd = input()
        if cmd.strip().lower() in ["exit", "quit"]:
            break
        log.append(f"λ {cmd}")
        handle_command(cmd)

if __name__ == "__main__":
    shell()
