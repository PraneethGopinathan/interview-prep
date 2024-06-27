## Answers to your questions:

### Question: 1

```python
def f(s):
r = {}
for i in s:
     if i in r:
         r[i] += 1
     else:
         r[i] = 0
return r
```


1. Tell us what this code does. Describe what it does in English as if you would write documentation for this. Justify your answers. 
2. Suggest ways to improve this code. Different approaches, code quality etc. 
3. Write unit tests for this code. 

**Answers:**

1.  This function takes a string 's' as input and returns a dictionary 'r' where the keys are characters from the string and the values are the counts of how many times each character appears in the string. So basically it simply returns the number of occurrences of character in the string.
Parameters:
s (str): The input string to be processed.
Returns:
r (dict): A dictionary with characters as keys and their respective counts as values.

2. There is a logical error in the else statement, instead of assigning 0 we should assign r[i] = 1, else we will get 0 for the first occurrence and if a character occurs twice it will show 1 instead of storing the exact occurrences and goes on, which is the total number of occurrences-1 will be stored as value.


    ```python
    # else r[i]=0
    python3 question1.py  #praneeth
    {'p': 0, 'r': 0, 'a': 0, 'n': 0, 'e': 1, 't': 0, 'h': 0}

    # else r[i]=1
    python3 question1.py # praneeth
    {'p': 1, 'r': 1, 'a': 1, 'n': 1, 'e': 2, 't': 1, 'h': 1}
    ```

3. Unitest: **_Pytest_** is the package I use to test the FastAPI framework so using the same here [question1.py](question1.py)

---
### Question 2:
Tell us about a scenario where you had to make changes to an existing Infrastructure-as-code setup to introduce a new change/fix a bug. What are the challenges you faced? How did you go about understanding other people's IAC code and modifying it?

**Answers:**

**_Since_** we are following the GitOps methodology all the IAC code is stored in our repository, and if I want to make any change/fix a bug I first create a corresponding branch associated with my JIRA task ID and do all the changes and commit and push the code. Once my team lead reviews the code thus raises an MR and finally merge it to the main branch after all the review comments are resolved (if any). 

**_The challenges that I faced_** are few like one is how to store the terraform state file in the backend S3 with state locking mechanism (AWS) and in Blob (Azure). So creating the buckets/blob as well needs to be in terraform script then only it will make it an end-to-end IAC. The other challenges would be like after successfully setting up the Kubernetes ie EKS cluster via Terraform next is to run our entire application via Helm and ArgoCD methodology. Once the development is completed we are moving for production level for that initially we plan to go with Terraform workspace methodology and later we decided to use the folder structured method when we found that the terraform workspace have some downsides.

**_Before modifying_** other people's code first I read the readme file (if any) to get the overall understanding of the code. If there is no such documention then I will cross veryfy all the modules and resources that are created with official terraform documentation page. But before doing that I will definetely check the terraform version that can be found in the `provider.tf` file to ensure whether I checking with the right version of the documention that is matched with my terraform code.