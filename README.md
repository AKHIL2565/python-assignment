<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Akhilesh Ravi (ar2565)</td></tr>
<tr><td> <em>Generated: </em> 3/23/2023 2:23:20 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/ar2565" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013069-33014b55-29c3-46aa-93b4-25b42b7bd6f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image shows the code for calculation of cost of the burger and<br>appending $ before the price and returning it<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013147-3fba2ac6-87c8-4999-971e-f6fe78a3bb41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The input statement here, gets the returned value of def calculate_cost() and prints<br>the amount in currency format and the user enters amount in $ format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>def calculate_cost() calculates the total cost of a burger based on its layers.<br>It first initializes a variable called price to 0.<div><br></div><div>Then, it loops over each<br>layer of the burger stored in the inprogress_burger . For each layer, it<br>accesses the cost attribute of that layer and adds it to the price<br>variable.</div><div><br></div><div>Finally, the method returns a string formatted with the total cost of the<br>burger to two decimal places, with a dollar sign prefix.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230031285-e1d0ccc2-a474-4f39-8243-b42ec9656295.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this image shows that out of stock exception is printed as there is<br>no stock of turkey patty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013558-2840d871-3ba2-48db-b55b-80eab8c9dc2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image shows the successful clean as the input entered is &quot;clean&quot;.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013614-0536f3f3-e67c-4181-970e-0bfeb85ddcbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image shows &quot;clean not succcesful &quot; because the entered input is not<br>&quot;clean&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013643-4926ada9-ec26-4cf7-a991-ce14915c38bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image shows invalid choice exception as the entered inputs are not correct<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013921-47bd96a1-fe10-43d8-befb-39baef6422cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this image shows the exceeded choices exception as I have given the input<br>of beef and mayo more than 3 times<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230013939-1c5a684f-c531-46c0-8c2a-4e58290b37a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>As the amount entered is wrong, the code raised an exception and asked<br>to enter the amount again<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>In the out of stock exception, If the currently selecting stage is Bun,<br>Patty or Toppings and it is out of stock, the program will print<br>a message indicating that the stage is out of stock and it will<br>move on to the next stage.<div><br></div><div>needs cleaning exception prompts the user to input<br>a message to indicate whether they want to clean the machine or not.<br>If the user enters &#39;clean&#39;, it calls the clean_machine() method to clean the<br>machine and prints a message indicating that the cleaning was successful. If the<br>user does not enter &#39;clean&#39;, it prints a message indicating that the cleaning<br>was not successful.<br></div><div><br></div><div>InvalidChoiceException is raised when the user selects an invalid option while<br>ordering a burger and prints an appropriate error message to the user specifying<br>that the choice they have made for that particular stage is invalid. If<br>the current stage is STAGE.Bun, the message will say &quot;the choice you have<br>chosen for Bun is invalid&quot;, and so on for the other stages.<br></div><div><br></div><div>If the<br>choices are exceeded more&nbsp; than 3, exceeded choice exception is raised. If the<br>current stage is Toppings and the exception is raised, the message printed is<br>&quot;the choice for the toppings has been exceeded. So, moving to the next<br>stage&quot; and the value of self.currently_selecting is set to Pay.&nbsp;<br></div><div><br></div><div>If the cost of<br>the burger is not entered properly, then this invalid exception is raised</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230014387-0c0a58dd-b514-4eb0-917b-d4a77adef718.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It raises an invalid stage exception as bun is not found in the<br>first place<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230014484-2c432e43-b680-49f7-80d7-bd70052d136e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This checks whether there is stock availability of patties. It raises out of<br>stock exception as veggies are set to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230015747-5ee3adc2-cb18-4e8d-a63e-c6895ef6ea32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This checks whether there is stock availability of toppings.It raises out of stock<br>exception as lettuce are set to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230015832-fc1c7492-2cc4-4fbb-abfc-c1693ac1b137.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>If patties are more than 3, exception is raised<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230015831-54e4cd5c-f380-4f2f-80a3-1b4069e71511.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>If toppings are more than 3, exception is raised<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230015829-ef3e1165-47bc-4150-b76b-5df6cf484aef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This calculates the cost of 3 different combinations of burger<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230016214-a6482344-3757-4e12-8407-418793e78176.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code calculates the sum of costs of different burgers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230016230-3955ba94-06ff-4f1b-8bb8-090aa9500400.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code calculates the increment of the total number of burgers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230016576-166f8070-1551-4683-acdb-d843c7673e3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>These are the overall execution of all the test cases using pytest -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>The first test function, test_bun_is_the_first, tests that an InvalidStageException is raised if a<br>patty or a topping is added before the bun.As the first input is<br>turkey i,e a patty, it raised an exception</div><div><br></div><div>The second test function, patty_is_in_stock, tests<br>that an OutOfStockException is raised if the quantity of a patty is zero.Here<br>patties[1] is set to 0 i,e veggies are set to 0. So, it<br>veggies are added, then</div><div>it shows outofstckexception</div><div><br></div><div>The third test function, toppings_in_stock, tests that an<br>OutOfStockException is raised if the quantity of a topping is zero.Here toppings[0] is<br>set to 0 i,e lettuce are set to 0. So, it lettuce are<br>added, then</div><div>it shows outofstckexception</div><div><br></div><div>The fourth test function, test_patty_is_three, tests that an ExceededRemainingChoicesException is<br>raised if more than three patties are added.Here , 4 patties are added<br>and the exception is raised</div><div><br></div><div>The fifth test function, test_toppings_are_three, tests that an ExceededRemainingChoicesException<br>is raised if more than three toppings are added.&nbsp;</div><div>Here , 4 toppings are<br>added and the exception is raised</div><div><br></div><div>The sixth test function, test_cost_of_burger, tests that the<br>cost of a burger is calculated correctly. 3 different burgers are given and<br>cost of the burger is checked by assert keyword</div><div><br></div><div>The seventh test function, test_total_number_of_burgers,<br>tests the total number of burgers made, is calculated correctly or not. Total<br>burgers are calculated by handle_pay()</div><div><br></div><div>The eight test function, test_total_number_of_sales, tests that total number<br>of sales made is calculated correctly or not</div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/6">https://github.com/AKHIL2565/python-assignment/pull/6</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I have learnt to execute a project by testing the testcases with pytest<br>fixtures and also I have learnt about the raising of different exception handling<br>techniques, appending into the list ,&nbsp;<div>calculating the sum of the list etc.<div>I have<br>gone through some issues while writing the test cases but eventually I have<br>learnt how to code them and executed all the test cases using -rA.</div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/230017245-3a9b2a13-f411-4f8e-a0f1-47d3c3a632c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the overall execution of the code with 2 different burger combinations<br>along with the calculation of the cost<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/ar2565" target="_blank">Grading</a></td></tr></table>
