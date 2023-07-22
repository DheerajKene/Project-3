import instaloader
Profile_name = input("Enter Insta Profile name: ")
print("Downloading data...")
instaloader.Instaloader().download_profile(Profile_name, profile_pic_only=True)
print("Download Completed!")
