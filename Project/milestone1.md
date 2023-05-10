<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Akhilesh Ravi (ar2565)</td></tr>
<tr><td> <em>Generated: </em> 5/10/2023 7:41:51 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/ar2565" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid E-mail validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="p d m " src="https://github.com/AKHIL2565/python-assignment/assets/123112989/50eaaa2c-5d60-411b-8f89-1959ce9d6806">      <br>[passwords do not match ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="e n a " src="https://github.com/AKHIL2565/python-assignment/assets/123112989/77e72c78-d298-4758-a31f-ecea2b5ad5a0"> [email not available ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 01 35 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/240f4d21-7e5e-42e6-bd05-a2e08933655a"> [chosen username not<br>available ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 04 14 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/921babf8-7bb5-4124-b346-e39f49134a7c"> [form with valid<br>data filled in it ] <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 11 58 32 AM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/2060c0f5-c266-4adb-9f38-59ac6717eb36"> [screenshot showing the<br>valid user data ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>We utilize WT-forms for form generation and validation. The form submission will attempt</div><div>to<br>deliver data to our Python POST route, which will extract the data and<br>run an insert query to our sample table.WT-form validators are used to validate<br>data both in frontend &amp; backend, username is validated to be of length<br>between 2 &amp; 30 characters and it shouldn't be previously used by another<br>user, email validation is done using an email validator.password &amp; confirm password should<br>both be the same and should be of a length of 8, This<br>is validated using wtform validators and it is stored in the database after<br>hashing it using the bcrypt hashing algorithm- email, username, and hashed password is<br>stored in the users table.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 13 54 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/7ca25f7b-e822-4e30-8bbd-f18152fa1911"> [password mismatch validation<br>]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 16 24 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/374201a6-ee33-48b7-88ac-abff22a3009d">[invalid user validation ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 17 41 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/81954d54-2355-49d0-be8a-a1fee37b9b57"> [ login successful]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>We have handled the login form using wt forms, which is similar to<br>how we handle register forms, but we'll utilize the username or email field<br>instead of the confirm password field. In the front end, if the username<br>or email field checks if data is entered or not, and if the<br>field has '@' it will use an email validator else it checks for<br>the username format, if the length is between 2 &amp; 30 or not,<br>and checks if the password is entered or not.&nbsp;</div><div>In the backend, we fetch<br>the data from the users table by passing the email/username, if we get<br>something we compare the password &amp;then check if the user is assigned roles.<br>In the front end, we first check if the password is entered &amp;<br>then in the back we fetch the password from the database based on<br>username/email &amp; then check if the passwords match, if they match then we<br>delete the password from that point in the program. &nbsp;we fetch username, email,<br>password from users table passing username/email, and then check if passwords match, and<br>then check if the user is assigned is any roles from userroles tables<br>&amp; fetch it.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 23 11 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4088bc42-fc95-49eb-add7-bf15ecfc73b9"> [logged out successfully<br>]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 27 30 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/372d0f65-2442-458f-90e2-d0df6de3138d"> [ message about<br>nit being logged in ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href=" https://github.com/AKHIL2565/python-assignment/pull/9"> https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>we use flask_login package to work with user session &amp; manage it, &nbsp;In<br>our main.py we’ll utilize LoginManager, this handles our user session and provides helpful<br>utilities Since we’re using an app factory we’ll defined a variable for login_manager<br>outside of the factory, then inside the factory we use its init_app() method<br>to associate the app . Next, inside of the app factory we’ll use<br>the user_loader decorator, this will run a process to lookup a user by<br>id</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 27 30 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/372d0f65-2442-458f-90e2-d0df6de3138d"> [ message about<br>nit being logged in ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 32 44 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/7d562da9-5d57-4ea2-aa9e-bd2e07e243a9"> [message about not<br>habving the appropriate role ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 12 21 44 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/bc388114-c898-4775-8a7e-2597c07d5d4e"> [screenshots of the<br>roles table with valid data having at least one variable in it ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 12 25 30 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/86eab869-3b82-4044-8e11-8430963f8fb5"> [screenshot of the<br>user roles table with valid data in it ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>Since we’re using an app factory we’ll defined a variable for login_manager outside<br>of the factory, then inside the factory we use its init_app() method to<br>associate the app,For the login protected pages, we decorate the views with @login_required<br>function, If the user is not logged in, it calls the LoginManager.unauthorized function.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>similar to login protected page, here we use @admin_permission_require function from roles.permissions package,<br>If the user is not a admin, &nbsp;we raise 403 exception and display<br>403 html page saying permission denied.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 48 16 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/b2900570-df37-4a12-bc30-f1f7bde030be"> [navigation bar with<br>a clean UI]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>using Bootstrap, a navigation bar can extend or collapse, depending on the screen<br>size. A standard navigation bar is created with the .navbar class,followed by a<br>responsive extend and collapsing class collapse. navbar-collapse for grouping and hiding navbar contents<br>by a parent breakpoint. navbar-brand for your company, product, or project name. navbar-toggler<br>for use with our collapse plugin and other navigation toggling behaviors. Using the<br>nav-item class allows developers to quickly change between different types of navigation in<br>the bootstrap system while only changing the wrapping class on the &lt;ul&gt; .<br>and Containers are a fundamental building block of Bootstrap that contain, pad, and<br>align your content within a given device or viewport.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 55 21 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/78797528-3f3b-4085-a424-26aa69b3c271">[message about not being<br>logged in ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 32 44 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/52d3420d-6aa7-4af4-9f64-cbec1450343d">[ message about not<br>having proper role or administration ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 6 58 57 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/8a9932f4-34de-45d4-8aec-342196ca83c2">[ error pops up<br>when the correct password is not entered ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>To better handle this, we have created two functions in main.py that’ll return<br>a render_template() to new respective files for 403 (access denied) and 404 (page<br>not found) For sake of simplicity ,these files are identical and just have<br>a basic user friendly messages applied, can customize these as we wish The<br>main purpose for this is to include our navigation to allow our user<br>to easily navigate to a proper location.And also included some flash messages which<br>will guide the users where they did wrong and which helps then recorrect<br>the data.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 02 08 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/6efe3142-a44a-45cc-bde9-279fd74c0c26"> [user profile page<br>where the details are properly pre filled ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>when profile page is opened, if it is not a POST request then<br>email, username are fetched from users table passing user id, then the are<br>rendered into the profile form.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 06 19 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/170f11f9-ffb7-477b-adf9-6e4bcae84081"> [message telling that<br>username is validated ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 07 42 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4c72285b-8f38-4443-94d0-679eb46fb0c6">[showing email changed message<br>which tells us that the email is validated ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 09 50 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/e727749e-89fc-4947-835e-943e9c683bbf"> [showing password changed<br>message which tells us that the password has been changed ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 11 36 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/0b9660eb-be11-4b0f-8c69-c0af3a1a1e36"> [password mis match<br>message ] <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 13 49 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/828c1461-1d74-4c66-8a1b-173d0db760e0">[message showing email already<br>in use ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 15 49 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/e68a8423-abff-476a-a286-37d62b2f56c1"> [message showing that<br>username is already in use ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 12 29 09 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/a7c90598-41d3-45d7-9b37-22bf46c67533"> [ screenshot of<br>the user table before the edit ] <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236964253-e86f2ad6-a86a-4305-a5d9-be68b90ce2a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img src="https://github.com/AKHIL2565/python-assignment/assets/123112989/c6a06c77-4784-4191-a960-2624c45475b5" alt="Screenshot 2023-05-10 at 12 32 19 PM"> [ screenshot of the user table<br>after the edit has been done in the email ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>the code first checks for if it is POST request, if it is,<br>then it checks if current_password, password &amp; confirm are given, then it retrieves<br>password from users table, then the current password &amp; pwd from DB are<br>compared to check if they are the same or not, if they are<br>not same we will raise a invalid password flask, if they are same<br>then the new password is hashed &amp; updated in the database. Then the<br>username &amp; email are updated in the database and a flash message &quot;saved<br>profile&quot; is displayed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>By doing this milestone I have got a chance to learn about user<br>login session, login/registration system, an authentication system ,Able to integrate the DataBase utility<br>and manage the website by storing and retrieving the data from the database&nbsp;</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/landing-page">https://is601-ar2565-prod.herokuapp.com/landing-page</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/ar2565" target="_blank">Grading</a></td></tr></table>
