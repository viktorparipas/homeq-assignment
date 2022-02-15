# The assignment

This assignment is a rough starting point for the backend & frontend
assignment. Depending on your specialty you can find details below.
If you are applying as a fullstack developer you should look at both
sections below.

## Backend assignment

The backend assignment will focus on API design and making sure there
is new functionality exposed to the frontend. As you can see there
is already a list of apartments you are starting out with. Other 
functionality should be implemented:

Customers should be able to:

- update, delete & create apartments
- be able to group apartments into buildings
- create a rental agreement for an apartment

Additionally, you can add users and companies such that the system 
can be used by multiple companies in parallel. If you have other 
ideas to show what you can do on top of the above-mentioned tasks 
feel free to continue but remember that the whole time invested 
should not exceed 6-8 hours. 

### Prerequisites for running

- Docker installed
- You will need to have the following ports free:
  - `3000` (client)
  - `8000` (service)
  - `5432` (postgres)

### Instructions
1. Clone repository
2. Setup a new repository with the source code
3. Run `docker-compose up`
4. Code
5. Push your solution and reach out to us for setting up the interview

To cleanup the Docker containers run `docker-compose down -v --rmi all --remove-orphans`
If you need to reset the database you need to delete the folder `data/db`
## FAQ
#### How will I be evaluated?
We are going to discuss the solution with you when we have a meeting. It is important to understand your
thinking and reasoning more than the actual code. During the discussion it helps us to understand your strengths 
and where you could improve.

Things we will take a look at
- **Code quality** - How you reason about making sure code is readable and maintainable.
- **Testing** - How you reason about what to test and how to test it.
- **Performance** - How you can identify performance bottlenecks and reason around solving them.
- **System design** - How you reason about concepts like reusability, separation of concerns and various abstractions.
- **Infrastructure and operations** - How you would run a system and what's important to think about.

In this we also try to understand how you solve problems generally and how you communicate your solutions. 
Problem solving and communication are both things we value highly.

#### Can I change things in the existing code?
Of course, you can make changes and explain why you make those choices. 

#### Can I use additional libraries/frameworks?
You can use whatever you want as long as you can explain your choices.
However, we recommend to not go to experimental with exotic libraries.

### What if I get stuck?
If you get stuck with the assignment you can reach out to your contact at HomeQ.
We will check with you and try to help you to move forward.  
