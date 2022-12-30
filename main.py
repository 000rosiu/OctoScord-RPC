import win32gui
import win32con
import discord_rpc

hwnd = win32gui.GetForegroundWindow()
window_title = win32gui.GetWindowText(hwnd)

current_window = window_title

prev_hwnd = win32gui.GetWindow(hwnd, win32con.GW_HWNDPREV)
prev_window = win32gui.GetWindowText(prev_hwnd)

rpc = discord_rpc.DiscordRPC()
rpc.set_presence(
    details=f"Currently using: {current_window}",
    state=f"Previously used: {prev_window}"
)

rpc.send_presence()
