import sys
sys.path.append('/usr/bin/python')
import cv2 
import face_recognition
import pickle


#ENTERING THE NAME AND ID OF THE EMPLOYEE


name	=	input("Enter Employee Name: ")
ref_id	=	input("Enter Employee ID: ")



try:
	f=open("ref_name.pkl","rb")
	ref_dictt=pickle.load(f)
	f.close()
except:
	ref_dictt={}
ref_dictt[ref_id]=name



f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f)
f.close()



try:
	f=open("ref_embed.pkl","rb")

	embed_dictt=pickle.load(f)
	f.close()
except:
	embed_dictt={}



for i in range(5):																				# WE TAKE 5 PICTURES FOR INSTANCE
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0)																# ACCESSING THE CAMERA
	while True:
		check, frame = webcam.read()
		cv2.imshow("Capturing", frame)
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		rgb_small_frame = small_frame[:, :, ::-1]
		key = cv2.waitKey(1)
		if key == ord('s') : 																	# WE STORE THE IMAGE WHEN WE PRESS KEY "S"
			face_locations = face_recognition.face_locations(rgb_small_frame)			
			if face_locations != []:
				print('Taken Picture')
				face_encoding = face_recognition.face_encodings(frame)[0]
				if ref_id in embed_dictt:
					embed_dictt[ref_id]+=[face_encoding]
				else:
					embed_dictt[ref_id]=[face_encoding]
				webcam.release()
				cv2.waitKey(1)
				cv2.destroyAllWindows()     
				break
		elif key == ord('q'):																	# WE EXIT THE WINDOW WHEN WE PRESS KEY "Q"				
			print("PRESSED Q: TURNING OFF THE CAMERA....")
			webcam.release()
			print("CAMERA IS TURNED OFF")
			print("PROGRAM IS ENDED SUCCESSFULLY")
			cv2.destroyAllWindows()
			break
f=open("ref_embed.pkl","wb")
pickle.dump(embed_dictt,f)
f.close()