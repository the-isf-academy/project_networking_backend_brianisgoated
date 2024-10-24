# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
*Replace this with an overview of your API.*

### Model

### Endpoints
| End points  | Description  |  Example |  Request |  Payload |
|---|---|---|---|---|
|  user_comments | allows the user to add or change a comment that other users have inputed  | comment: "I find this drill really helpful"|  post |  new_comment - str |
|   change_tip|   helps other users in the program to be able to complete the drill |  tip: "form a C while dribbling" | post  | new_tip - str  |
| add_likes | a user can like the drill if they find it useful or enjoy doing it  |   drill: crossover, like: 3|  post | add_likes - int|
  |

*Replace this with a guide to your endpoints and model. You can write a Markdown chart [here](https://www.tablesgenerator.com/markdown_tables)*

---

## Setup

### Contents
 
Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



