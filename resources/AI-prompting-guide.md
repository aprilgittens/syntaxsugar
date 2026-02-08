## Overview

This guide contains effective prompts for using AI coding assistants (like GitHub Copilot, ChatGPT, Claude, etc.) to learn Python. These prompts are organized by topic and designed to help you understand concepts, not just get answers.

**Remember:** When learning a programming language, use AI as a tutor, not a solution machine! Always try to understand *why* something works, not just *that* it works.


## Stream 1: Environment Setup

### Installation & Setup

**Verifying Python Installation**

```
I just installed Python. How do I check if it's installed correctly?

```

**PATH Issues (Windows)**

```
When I type 'python' in Command Prompt, it says 'python is not recognized as an internal or external command'. What does this mean and how do I fix it?

```

```
Can you walk me through adding Python to PATH on Windows step-by-step?

```

**Python vs Python3 (Mac/Linux)**

```
On my Mac, when I type 'python --version' it shows Python 2.7. I installed Python 3.12. What's going on?

```

### VS Code Setup

**Understanding VS Code**

```
I'm new to VS Code. What are the main parts of the interface I should know about?

```

**Extensions**

```
What does the Python extension for VS Code actually do? Why do I need it?

```

**Running Python Files**

```
I created a .py file. How do I run it in VS Code?

```

#

### First Python Program

**Understanding print()**

```
What does the print() function do in Python? Why do we need the parentheses?

```

**File Extensions**

```
Why do Python files need to end in .py? What happens if I don't use that extension?

```

**Understanding Output**

```
I ran my Python file and saw text appear in the terminal. Where does that output come from?

```


## Stream 2: Variables and Data Types

### Variables - Basics

**Understanding Variables**

```
Explain what a variable is in Python using a simple analogy.

```

```
What's the difference between a variable name and the value it stores?

```

**Variable Assignment**

```
What does the = sign mean in Python? Is it the same as "equals" in math?

```

```
Can I create a variable without assigning it a value?

```

**Updating Variables**

```
When I write 'score = score + 1', how does Python know what 'score' is on the right side?

```

### Variable Naming

**Naming Rules**

```
What are the rules for naming variables in Python? What characters can and can't I use?

```

```
Why can't I use spaces in variable names? What should I use instead?

```

**Naming Conventions**

```
What's the difference between snake_case, camelCase, and PascalCase? Which should I use in Python?

```

```
Is 'user_age' or 'userAge' better for Python? Why?

```

**Good Naming Practices**

```
What's wrong with this variable name: '2nd_place'?

```

```
I have a variable 'x' that stores an email address. Suggest a better name and explain why it's better.

```

```
What are some examples of good vs bad variable names for storing a person's phone number?

```

### Strings

**String Basics**

```
What's the difference between "hello" with double quotes and 'hello' with single quotes?

```

```
I want to combine two strings. How do I do that?

```


**String Methods**

```
What are some useful things I can do with strings in Python?

```

### Integers

**Integer Basics**

```
What's an integer in Python? Give me 5 examples.

```

```
What's the difference between 25 and "25"?

```

**Integer Math**

```
What's the difference between / and // in Python?

```

```
What does the % operator do? Give me an example.

```

```
I divided two integers and got a decimal number. Why did that happen?

```

### Floats

**Float Basics**

```
What's a float in Python? When should I use a float instead of an integer?

```

```
What's the difference between 5 and 5.0?

```

**Float Precision**

```
Why does 0.1 + 0.2 not equal 0.3 in Python? Is this a bug?

```

```
Should I use int or float for storing money amounts? Why?

```

**Float Operations**

```
When I multiply an integer and a float, what type is the result?

```

### Booleans

**Comparisons**

```
What's the difference between = and == in Python?

```

```
Explain each of these comparison operators: >, <, >=, <=, ==, !=

```

```
When I write 'age > 18', what type is the result?

```

### Type Checking

**Using type()**

```
What does the type() function do? When would I use it?

```

```
I see '<class 'str'>' when I use type(). What does that mean?

```

**Type Confusion**

```
These all look similar: 5, 5.0, "5", True. What type is each one?

```

### Type Conversion

**String to Number**

```
How do I convert the string "25" to a number so I can do math with it?

```

```
I'm getting "ValueError: invalid literal for int()". What does this mean?

```

**Number to String**

```
How do I convert a number to a string so I can combine it with text?

```

**Complex Conversions**

```
How do I convert the string "19.99" to an integer?

```

```
What happens when I do int(3.9)? Does it round up or down?

```

### Debugging Type Errors

**Understanding Error Messages**

```
I got this error: "TypeError: can only concatenate str (not "int") to str"
What does it mean and how do I fix it?

```

```
I'm trying to add "Age: " + 25 but getting an error. What's wrong?

```

```
Explain this error: "ValueError: invalid literal for int() with base 10: '25.5'"

```

**Fixing Type Issues**

```
I have age = "25" and I want to calculate next_year = age + 1. How do I fix this?

```

```
Why isn't this working: print("Total: $" + 19.99)?

```

### Understanding Code

**Code Explanation**

```
Explain what this code does line by line:
[paste your code]

```

```
I wrote this code but I'm not sure if it's correct. Can you review it?
[paste your code]

```

### Practice & Learning

**Getting Examples**

```
Give me 3 practice problems for working with variables and data types, from easy to hard.

```

```
Show me an example of when I would need to convert from string to int in a real program.

```

**Concept Clarification**

```
I'm confused about when to use int vs float. Can you give me clear examples of when to use each?

```

**Testing Understanding**

```
Can you quiz me on variables and data types? Ask me one question at a time.

```

```
I think I understand strings vs integers. Can you give me a tricky example to test my understanding?

```

## Effective Prompting Tips

### Be Specific

```
❌ Vague: "Help with my code"
✅ Specific: "I'm getting a TypeError when trying to add a string and number. Here's my code: [paste]"

```

### Provide Context

```
❌ No context: "What's a variable?"
✅ With context: "I'm brand new to Python. Can you explain what a variable is using a simple analogy?"

```

### Ask for Explanations

```
❌ Just answers: "How do I convert string to int?"
✅ With reasoning: "How do I convert string to int? Also explain why the conversion is necessary."

```

### Request Examples

```
❌ Theory only: "Explain type conversion"
✅ With examples: "Explain type conversion and give me 3 practical examples of when I'd need it"

```

### Follow Up

```
First: "What's the difference between int and float?"
Then: "Can you give me examples where using the wrong one would cause problems?"
Finally: "Show me how to convert between them"

```

## Prompt Templates

### Understanding Errors

```
I got this error: [paste complete error message]
1. What does it mean in simple terms?
2. What likely caused it?
3. How do I fix it?

```

### Explaining Code

```
Can you explain this code line by line in simple terms?
[paste code]

Also tell me:
- What type is each variable?
- What's the final output?
- Are there any potential issues?

```

### Concept Clarification

```
I'm learning about [topic]. I understand [what I know] but I'm confused about [what I don't understand]. Can you explain with an example?

```

### Debugging Help

```
I'm trying to [describe goal] but [describe problem].

Here's my code:
[paste code]

Here's the error (if any):
[paste error]

What am I doing wrong?

```

### Practice Request

```
I just learned about [topic]. Can you give me:
1. An easy practice problem
2. A medium problem
3. A challenge problem

Let me solve them myself, then I'll ask for solutions.

```

## Remember

### AI is a Tool, Not a Teacher Replacement

- AI gives information, YOU build understanding
- Always test what AI suggests
- Ask "why" not just "how"
- Struggle before asking - that's where learning happens!

### When AI Might Be Wrong

- AI sometimes makes mistakes
- Verify suggestions by running code
- Check official Python documentation for critical info
- If something seems off, ask AI to explain further

### Best Practices

1. **Try first, ask second** - Attempt problems yourself
2. **Run the code** - Don't just read AI's response
3. **Ask follow-ups** - "Why does this work?"
4. **Explain it back** - If you can't explain it, you don't understand it
5. **Use multiple sources** - Combine AI, docs, and practice


---

Keep this guide handy while coding! Add your own prompts as you discover what works for you.