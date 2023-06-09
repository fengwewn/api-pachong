from pynput import mouse

def on_click(x, y, button, pressed):
    while True:
        if button == mouse.Button.left:
            print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
            break
        else:
            print('{} at {}'.format('Pressed Right Click' if pressed else 'Released Right Click', (x, y)))
            break

listener = mouse.Listener(on_click=on_click)
listener.start()

# 等待鼠标监听器结束
listener.join()
