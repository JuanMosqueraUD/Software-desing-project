# Software modeling - Question and Answers platform
 
This project aims to develop a ___backend___ for a question and answer forum similar to Reddit, using creational and design patterns. The project is implemented in Python and hosted in a GitHub repository for the ___software modeling subject___.

## Definition



### Stackerholders

- __Users__: Users are the people who interact with the forum, either to post questions, answer them, or read other people's answers.
- __Administrators__: Administrators are responsible for moderating the forum content, deleting inappropriate posts, and managing user accounts.
- __Developers__: Developers are responsible for creating and maintaining the forum backend.

### Business model

The forum's ___business model___ is based on __advertising__ and __user voluntary donations__. Users can see ads while browsing the forum. Advertisers pay to place their ads on the forum and user pay to be ad free.


### Tools to use

- __Python__: Programming language used to develop the forum backend.
- __Django__: Web framework used to develop the forum frontend.
- __GitHub__: Platform used to host the project source code.
- __Vs code__: Main IDE for development.

## User Stories

- __As a__ user, __I want__ to be able to post a question, __so that__ I can get help from the community.

- __As a__ user, __I want__ to be able to answer a question, 
__so that__ I can help other users. 

- __As a__ user, __I want__ to be able to vote on a question or answer, __so that__ I can indicate the quality of the content.
- __As a__ user, __I want__ to be able to search for questions and answers, __so that__ I can find the information I need.

- __As an__ administrator, __I want__ to be able to delete inappropriate posts, __so that__ I can keep the forum clean and safe.

- __As an__ administrator, __I want__ to be able to manage user accounts, __so that__ I can control who has access to the forum.

## Entities

- User: username, id, email, pasword, post_question(), vote_question(), comment_post(), Question[E],Answer[E]. 
- Question: question_id, title, body, creation_date, User[E], vote count. 
- Answer: Question[E], body, creation_date, vote_count, User[E]
- Administrator(User): delete_post(), delete_answer(), ban_user().

## Processes

- User Registration:

![activity diagram](docs\images\Diagrama_de_actividades1.png)

- User Login
- Posting Question
- Posting Answer
- Voting Content
- Searching Content
- Moderating Content