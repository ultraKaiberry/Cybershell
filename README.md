# Cyber_shell
ui for command line 

This project of mine doesn't ship
or depend on any pentesting tools. it simply executes shell commands you enter
(like nmap,msfconsole,python3)if they already exist in ur system. you are full responsible for how you use this interface.

## 🔧 Add Your Own Commands

To add custom commands, open `cybershell.py` and scroll to the `handle_command()` function.

Use `elif` blocks to map new commands. Here’s the pattern:

```python
elif cmd.startswith("your-command"):
    os.system(cmd)
    log.append(f">> Executed: {cmd}")

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).  
Feel free to use, remix, and build upon it — just give credit. ❤️
