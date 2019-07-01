# Naarad

![Naarad Logo](/Logo.png)

The chivalrous messenger god is here to reduce your burden of Digital Publicity of your college events in facebook groups.

## Motivation

With every new event in college or any organisation, comes the burden of making it spread organically through facebook. A great way to do this is by posting it in multiple groups. It is a very tiresome and repetative task which can be excruciating at times.

## Features

- Allow posting in multiple groups by providing the list of groups and the required content.
- Accept list and content in multiple formats.
- Allow posting for two types of posts: embed and non embed.
- Allow posting a new post as well existing post.
- Create a installable pip package for the same.
- Secure and doesn't take password beyond user's system.

## Detailed Description

Below is a rough algorithm for the working of the application. This is to be improved as we move on with the project:

```text
Step: Take required input from the user
Step: Login to facebook with given credentials using web driver
Step: Selecting the type of post to be shared
Step: Open each link and using the web driver enter the form with data
Step: Post and show success message

The input taken will be:
- Phone Number / Email (for login)
- Password (for login)
- List of links (via batch file or entering manually)
- existing post or new post
- Text for the post
- Image / Link for the post
```

## Development Setup

The development environment requires a linux system with Python 3.7 and [clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) of the [forked version](https://help.github.com/en/articles/fork-a-repo) of this repository. 

#### Installing Pipenv

We are using Pipenv for managing project development in a virtual environment and it is also the package manager here.

[Why Pipenv?](https://opensource.com/article/18/2/why-python-devs-should-use-pipenv)

[Install Pipenv](https://www.linode.com/docs/development/python/manage-python-environments-pipenv/#install-pipenv)

#### Setting Environment First Time

Below commands will setup the environment for the first time.

```bash
cd /project/directory
pipenv shell --three
pipenv install --dev
```

#### Development Etiquettes

Please use `pipenv shell` to activate the already created virtual environment for the project (created in last step). 

Once in the virtual environment, use the command `pipenv install PACKAGE_NAME1 PACKAGE_NAME2` to install new packages.

**NOTE:** Do not install packages without pipenv. We will not be supporting requirements.txt standard. 

#### For Windows 

[Download](https://www.seleniumhq.org/download/) the web driver according to version/type of your browser. Make sure that EXE file downloaded is inside the the project folder. In your development environment you can run the py file.

## Schedule

#### Phase I

Explore all the options and the tools required to accomplish the same. Get a knowledge of the DOM structure of Facebook.

#### Phase II

Create a basic structure for the project and implement the extracting and selection of DOM objects required for the process. Acceptance of input and formatting it should also be completed.

#### Phase III

Make it a pip package and finish up the coding phase. Write tests if time remains.

## Contribution Guidelines

Please raise a feature request or issue before sending PR for the same.

Follow the below guidelines for proper coding practices:

- Always [create a new branch](https://confluence.atlassian.com/bitbucket/branching-a-repository-223217999.html) for your changes and make PR from it ONLY.
- Write neat code with proper comments.
- Follow PEP8 coding style.
- Write descriptive commit messages. Please [read this](https://github.com/erlang/otp/wiki/writing-good-commit-messages) for more information.
- Write detailed PR messages and include `fixes #ISSUE_NUMBER` it if closes an issue, otherwise use `concerns #ISSUE_NUMBER` to tag the related issues. Please [refer here](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/) for more PR guidelines.
- It is recommended to have a single commit for a task.
- Use [DRY principles](https://thealphadollar.github.io/learning/2019/05/13/go-dry.html) to create maintainable code.

## Communication
[Badges](https://img.shields.io/github/issues/oss2019/naarad.svg)
All contributors / users are requested to join [Gitter channel](https://gitter.im/oss2019/naarad) for further discussion on ideas, PRs and issues.

For issues please raise a ticket in the issues tab in the [Naarad github repository](https://www.github.com/oss2019/naarad).

Mentor for the project: [thealphadollar](https://www.github.com/thealphadollar/)

