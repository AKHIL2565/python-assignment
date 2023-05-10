<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Akhilesh Ravi (ar2565)</td></tr>
<tr><td> <em>Generated: </em> 5/10/2023 7:39:24 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/ar2565" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 33 23 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/ff6c50a7-d49f-4193-9342-db7e2fbea2d4"> [admin page created<br>a new item by giving valid data ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 12 42 08 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/12fbba49-5448-412a-a389-c4c31e9daf13"> [ screenshots showing<br>all the products and the latest added <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div>The values are sent to the item function in shop.py after being entered<br>on the add page. To determine if the action is to edit or<br>add, it looks to see if an id has been passed. This is<br>a create action since no id is supplied; hence, an INSERT statement is<br>executed passing the values to the Products table, and if successful, a flash<br>is shown.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/admin/item">https://is601-ar2565-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 44 19 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/cf8ed452-c638-4fd0-b6fc-0bdda0f22494"> [shop page showing<br>10 items ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 47 37 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/463bb8ff-e21c-41b7-9d8b-6cd735000e05"> [ screenshot showing<br>both the electronics &amp; price low to high filters ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 51 02 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/20237ee2-7a24-4d00-9f14-e6136ccbf8aa">[ screenshot showing different<br>filter and sorting methods ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="895" alt="Screenshot 2023-05-10 at 7 37 48 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4a6dcc81-1b43-48ab-819a-d236d4eb5c9a"> [screenshot of the<br>filter/sort logic from the code]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>Initial data for the shop page comes from the Products table, whose visibility<br>is set to 1. Moreover, the page allows for name searches, category selections,<br>and price &quot;High to Low&quot; or &quot;Low to High&quot; sorting. When we use<br>one or more of the aforementioned search options. We proceed to the shop.py<br>function&#39;s shop list and modify the query&#39;s where condition based on the input.and<br>then show the outcomes once more.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href=" https://github.com/AKHIL2565/python-assignment/pull/9"> https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/shop?name=&category=Food&price=ASC">https://is601-ar2565-prod.herokuapp.com/shop?name=&category=Food&price=ASC</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 7 56 18 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/c892158f-8472-46c6-ae40-e515538c89bf">[screenshots of admin list<br>, page/ results]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>Without applying any filters, we choose every field from the Products database and<br>feed it to the HTML page. Since no conditions are stated anywhere, every<br>product will be shown regardless of visibility status.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/admin/items">https://is601-ar2565-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 8 02 30 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4e8bf808-230d-457a-99a1-8dc7c5066a75"> [screenshot showing the<br>edit button available to the admin on the shop ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 9 58 31 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/efa01d79-b9aa-4f73-997d-8ea580786a4b"> [screenshot showing the<br>edit button visible to the Admin on the Product]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 10 00 23 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/a4aabdb0-650b-4446-9df2-da092f1a1566"> [screenshot showing the<br>edit button visible to the Admin on the admin product list page ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 10 12 09 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/8deda683-48cc-4690-a8af-439ede6c2084"> [ screenshot showing<br>the unedited item ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 10 12 20 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4fdff872-efac-4190-9185-f054801a378b"> [ screenshot showing<br>the updated item portfolio ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>Every product in shop.html has a check to see whether the user is<br>logged in and if they are an admin. If both are true, we<br>display an edit button that takes the user to the item page with<br>the product details. The edit button is displayed on the item details page<br>if the user is an admin. Since only administrators can access the page,<br>the edit button is the default on the admin items page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/admin/item?id=3">https://is601-ar2565-prod.herokuapp.com/admin/item?id=3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 10 20 12 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/ba8a97c4-efe3-4ead-85a8-96424450157b"> [ screenshot showing<br>the button that directs the user to the product details page ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-09 at 10 21 36 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/95fb3b62-62cc-4826-b944-5ae15604edc4"> [screenshot showing the<br>result of the product details page ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>For this, I made the itemdetails.html and item details functions. The product name<br>has been made clickable; when clicked, it will send the product id to<br>the item details function, which will retrieve all the information from the Products<br>database using the id and display it on the item details page.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href=" https://github.com/AKHIL2565/python-assignment/pull/9"> https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/itemdetails?id=3">https://is601-ar2565-prod.herokuapp.com/itemdetails?id=3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 05 46 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/a5fe5da5-67e5-41d8-9575-445966cf8e54"> [screenshot of the<br>success message of adding an item to the cart]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 07 03 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/b4ddc566-2408-4acd-b2eb-9b6665c59d77"> [ screenshot showing<br>an error when the user is not logged in ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 12 13 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/ab961c4f-d098-438d-b135-354135b53b67"> [this is the<br>screenshot of cart table with data in it ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <div>Product id and user id serve as the composite unique key for one<br>cart per user. And receives the products from the shop whenever a user<br>is added to the cart a insert query will perform that inserts the<br>data into the cart. and also perform an update and delete queries when<br>a user wants to update quantity or delete a product.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>When the amount field is provided to the cart function in shop.py by<br>clicking the ADD button, the product id is passed as a hidden field<br>and as long as the quantity is larger than 0, we insert the<br>product id, user id, desired quantity, and unit price (fetching it from products<br>table)<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 13 42 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/84711767-082d-4277-a7c4-d70746c5ec79"> [screenshot of the<br>cart view with the respective subtotal  ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>When we click the cart, the function checks to see if a product<br>id is being passed and, if it isn&#39;t, it recognizes that this isn&#39;t<br>an add or update function. It then moves to the SELECT block to<br>get the user id, id, product id, name, and desired quantity, calculates the<br>subtotal by multiplying the desired quantity by the unit price, and passes these<br>values to cart.html. For the purpose of calculating the total, we render each<br>item as a row in a table in the HTML output, add the<br>subtotal value for each row to a variable called ns.total, and then display<br>the total at the bottom.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/cart">https://is601-ar2565-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 15 49 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/d32620b5-4962-47c1-ba4f-8e25385e83c9"> [ Screenshot of<br>the cart before the quantity is updated ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img src="https://github.com/AKHIL2565/python-assignment/assets/123112989/9b0177e0-65b6-4307-a581-ca7d053fb3e5" alt="Screenshot 2023-05-10 at 1 17 55 PM"> [sCREENSHOT OF THE CART AFTER THE<br>QUANTITY OF AIRPODS HAS BEEN CHANGED SUCESSFULLY]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 19 27 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/0d7f3855-e4af-4e8d-aaed-89ae841dc92a"> [ screenshot before<br>the quantity has been updated to 0 ]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 20 44 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/bb7699e3-39bf-4552-aecf-e2c2d90e3551"> [ screenshot after<br>the item quantity has been set to 0 ]<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 20 44 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/bb7699e3-39bf-4552-aecf-e2c2d90e3551">(this is the screenshot<br>showing how a negative value is handled at the cart)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>When we press the update button next to the amount field and update<br>button in the cart, a concealed product id is sent to the cart<br>function. In the code, if the quantity is greater than 0, we first<br>retrieve the name and price from the products table before updating the quantity<br>and price in the cart table while supplying the product id and user<br>id. As the number is less than 0, when we enter 0 in<br>the quantity field, the code moves to the DELETE block, where we delete<br>the product from the cart database while passing the product id and user<br>id. We set the minimum value for the input field in HTML to<br>0 to handle negative values in the amount field.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 26 47 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/23524d42-1bce-4269-8ae2-126c8fae353e">(this is the screenshot<br>show the cart before deleting an item from the cart)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 27 05 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4a9f946f-b796-44f5-b368-e3b757a02c9e">(this is the screenshot<br>showing the cart after the item has been deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 31 28 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/4eae5748-6914-4a23-b8e5-f9424706734d">(this is the screenshot<br>showing before the cart has been cleared)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112989/236963579-7ed7c6d9-1bcb-4dfc-8953-907df4092df2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img width="1440" alt="Screenshot 2023-05-10 at 1 31 39 PM" src="https://github.com/AKHIL2565/python-assignment/assets/123112989/afdf477b-08a7-43e3-8187-d46092bbc390">(this is the screenshot<br>showing the cart after clearing the cart)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>When deleting a single item from a cart, a hidden field amount of<br>-&gt; will be supplied next to the delete button, and the cart function<br>will process the delete query while sending the product id if the number<br>is less than zero. When clearing the entire cart, we pass the variable<br>delete all with a value of 1, and if the delete all value<br>is True in the cart method, we delete the records in the Cart<br>table while passing the user id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AKHIL2565/python-assignment/pull/9">https://github.com/AKHIL2565/python-assignment/pull/9</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>One of the place where I got stuck was, while creating the tables,<br>the cart table is depend on product table and the query for creating<br>for cart table is before the creation of product table so there my<br>product table was created but the items were not able to get into<br>cart and later i noticed that there was no cart table created and<br>then i realize so i run inti_db.py again and the cart table was<br>created.And rest was all normal and got a chance to learn to build<br>the webpages in a real-life project.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2565-prod.herokuapp.com/cart?delete_all=1">https://is601-ar2565-prod.herokuapp.com/cart?delete_all=1</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/ar2565" target="_blank">Grading</a></td></tr></table>
