from capturatecla import KeyPressListener
import sys
while True:
    Key = KeyPressListener().get_key()
    if Key:
                print(f"Key pressed: {repr(Key)}")
                if Key == 'q':
                    break
                if 'M' in Key:
                    sys.stdout.write(f"\033[{Key[3]};{Key[2]}H")
                    print('#')
                    sys.stdout.write("\x1b[0G\x1b[K")