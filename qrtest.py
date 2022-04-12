import qrcode
img = qrcode.make('''
             Name: Rishabh Kumar.
             Instagram Link: https://www.instagram.com/_rishabh_yaduvanshi_/
             My All Android App Download Link: https://rishabhsahil.github.io/search.html?q=Rishabh%20app%20download#gsc.tab=0&gsc.q=Rishabh%20app%20download&gsc.page=1
             NCERT Books & Solutions App Download: https://play.google.com/store/apps/details?id=com.solutions.ncertbooks
             --- Technology is my life ---
        '''
 )
type(img)  # qrcode.image.pil.PilImage
img.save("TESTe.png")


# import qrcode module
import qrcode
 
# create QR code instance
qr = qrcode.QRCode(
	version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=1,
	border=1
)
 
# Enter data that you want to store
qr_data = '''
             Name: Rishabh Kumar.
             Instagram Link: https://www.instagram.com/_rishabh_yaduvanshi_/
             My All Android App Download Link: https://rishabhsahil.github.io/search.html?q=Rishabh%20app%20download#gsc.tab=0&gsc.q=Rishabh%20app%20download&gsc.page=1
             NCERT Books & Solutions App Download: https://play.google.com/store/apps/details?id=com.solutions.ncertbooks
             --- Technology is my life ---
        '''
 
# Add data 
qr.add_data(qr_data)
qr.make(fit=True)
 
# Create an image from the QR code instance
img = qr.make_image(fill_color='black', back_color='white')
 
# Save the image
img.save('rishabhdata2.png')

