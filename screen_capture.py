import win32gui, win32ui, win32con
import numpy as np
import cv2

def capture_runeLite_window(window_name):
    """Captures the RuneLite window as an image using Win32 API."""

    hwnd = win32gui.FindWindow(None, window_name)
    if not hwnd:
        print("❌ Error: RuneLite window not found.")
        return None, None

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width, height = right - left, bottom - top

    hdc = win32gui.GetWindowDC(hwnd)
    dc_obj = win32ui.CreateDCFromHandle(hdc)
    mem_dc = dc_obj.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(dc_obj, width, height)
    mem_dc.SelectObject(bmp)
    mem_dc.BitBlt((0, 0), (width, height), dc_obj, (0, 0), win32con.SRCCOPY)

    bmp_info = bmp.GetInfo()
    img = np.frombuffer(bmp.GetBitmapBits(True), dtype=np.uint8)
    img.shape = (bmp_info['bmHeight'], bmp_info['bmWidth'], 4)

    win32gui.DeleteObject(bmp.GetHandle())
    mem_dc.DeleteDC()
    dc_obj.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc)

    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR), (left, top, width, height)  # Keep OpenCV format in BGR

