class Image:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        # Simulate an expensive operation
        print(f"Loading image from {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def display(self):
        if self.image is None:
            self.image = Image(self.filename)
        self.image.display()

# Usage
proxy_image1 = ImageProxy("image1.png")
proxy_image2 = ImageProxy("image2.png")

# Image is not loaded yet
proxy_image1.display()  # Output: Loading image from image1.png
                        #         Displaying image1.png

# Image is already loaded, no need to load again
proxy_image1.display()  # Output: Displaying image1.png

# Image is not loaded yet
proxy_image2.display()  # Output: Loading image from image2.png
                        #         Displaying image2.png






# Explanation
# Image Class:

# Image represents an expensive-to-create object (loading an image from disk).
# The load_image method simulates a costly operation.
# ImageProxy Class:

# ImageProxy acts as a proxy to the Image class.
# It holds a reference to the real Image object, which is initially None.
# The display method checks if the image is already loaded. If not, it loads the image and then displays it.

# Usage:
# When proxy_image1.display() is called for the first time, the proxy creates the Image object and loads the image.
# Subsequent calls to proxy_image1.display() use the already loaded image.
# The same pattern applies to proxy_image2.

# Benefits of Proxy Pattern
# Lazy Initialization: Loading resources only when needed.
# Access Control: Restricting access to certain operations or objects.
# Logging and Auditing: Keeping track of access to the original object.
# Remote Access: Managing access to objects located on a remote server.

# Conclusion
# The Proxy Pattern is a powerful tool that allows you to add a layer of control and flexibility to how objects are accessed and utilized. Whether it's to defer expensive operations, enforce access rules, or add logging and monitoring capabilities, proxies provide a versatile solution for a variety of scenarios in software design.
