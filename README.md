# Soical Media Project With Live Chat and Video Conference System


**----------------------------------Introduction------------------------------------------**

**I am developing a django app for complete and fully functional social  media system with live chat and video conferecing system, where new user can do registraion and need to 
verifid account by email verification.  After verify the account user will redirect to profile setup page. User can submit their personal information for the profiel. With this
infomation each user profile will manage. User can do POST with image or without image. User can do like, comment and replay on the posts. User can edit/delete on his/her own 
post, comment and replay. User can also edit his own post and profile. Each will give permission like other social media for the edit and delete operation. User can search and for 
people and make new frineds by following them. User can also unfollow friends. User can also block users to avoid wrong things. User has a separate page for live chatting where 
user can filter the online and offline users and can do real time chatting. I have also implement a video conference system by used Zegocloud API where users can create new meeting
also can join other meeting by the link**




**----------------------------------User Requirements-----------------------------------**

1.	User Authentication and Authorization (Registraion, Email Verification, Login, Permissions)
2.	Profile Management
3.	Connection/Friend Management
4.	Post Management
5.	Like, Comment, Replay Management
6.	Follow Follwer Management
7.	Live Chatting Management
8.	Notification Management
9.	Video Conference System



**--------------------------------System Requirement-------------------------------------**

1.	User Registration:
•	Multiple Users can create accounts using their valid email.
•	User needs to provide First Name, Last Name, and Username
2.	Profile Management:
•	Users can set, edit, and delete their profile information like First name, last name, bio, address, country, about, profile picture, and other social media profile links.
3.	Friend/Connection Management:
•	Users can follow/unfollow other users.
•	The system will suggest unfollowed users to increase connections
•	Users can see their own Following & Followers
•	Users can also see others following & followers.
4.	Post Management:
•	Users can share their thoughts by posting status.
•	Status will appear on others' home page
•	User can see other posts and also their own post
•	User can edit, and delete their own post

5.	Like, Comment Management
•	Users can like, and comment on other's posts.
•	User can give a replay for the comment
•	User can unlike the post
•	The Post Owner can delete the comment
6.	Live Chat:
•	Users can engage in one-on-one chats.
•	All the registered users will be available on the chatting page
•	Users can see the online/offline status
•	User will get a notification for a new message

7.	Notifications:
•	Users receive real-time notifications for various activities, including messages, likes, and comments.
•	Notifications will be visible in the notification icon

8.	Video Conferencing:
•	Users can join video conferences with room ID.
•	Users can create video conferences with room ID.
•	The system supports multi-user video conferences.
•	User can turn on/off camera and mike



**----------------------------------Functional Requirements--------------------------**

1.	The user needs to verify the mail address, a Verification link will be sent to the email address.
2.	Only email Verified users can log in.
3.	The username must be unique.
4.	One email can allow for one account.
5.	User profile data will be saved and shown to the user profile.
6.	User can edit/delete their own post.
7.	Users can undo like on a post.
8.	Users can unfollow connections.
9.	Users can see the message time.
10.	All the messages will be saved in the database, with the time.
11.	User will get notifications for actions related to their profile.
12.	The user can turn on/off the camera and mike in a video conference.
13.	Users can search for other users, posts, or content using keywords, hashtags, or specific user names.



**-----------------------------Non-Functional Requirements---------------------------**
Performance:
•	The system has the ability to handle multiple users.
Security:
•	Secure user authentication and authorization mechanisms to protect user accounts and personal information.
•	Only verified user can login and see others profile.
Data Backup and Recovery:
•	All the data will be saved in database.
