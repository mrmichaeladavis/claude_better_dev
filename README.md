# AI Coding Assistant Experiment: Image Cropper

## Introduction

This repository contains experiments comparing the effectiveness of different system prompts for AI coding assistants. The experiments focus on fixing and testing an image cropping function, replicating and expanding upon the Claude 3.5 Sonnet demo.

## Background

### Claude 3.5 Sonnet Demo

In early 2024, Anthropic released a demo video showcasing their Claude 3.5 Sonnet model's ability to fix and test code. The demo featured a simple image cropping function with bugs that Claude was tasked to identify, fix, and create a test for.

### AI Coding Assistant Problem

A video, <https://www.youtube.com/watch?v=x0y1JWKSUp0> created by a well known youtuber, Internet of Bugs, a software professional with 35 years of experience, critically analyzed the Claude demo. The author highlighted several issues with AI coding assistants:

1. Inability to correctly identify and fix simple bugs
2. Poor test case generation that doesn't adequately verify functionality
3. Tendency to overcomplicate solutions when simpler fixes are available
4. Lack of judgment in choosing appropriate algorithms for different scenarios
5. Inadequate planning and estimation capabilities for software projects

These issues contribute to a broader concern about the current limitations of AI in software development and the potential risks of relying too heavily on AI coding assistants.

### Need for This Experiment

Given the critical analysis of the Claude demo and the broader concerns about AI coding assistants, this experiment was designed to:

1. Verify the claims made in the video about AI limitations in coding tasks
2. Explore whether different prompting strategies could improve AI performance
3. Provide a reproducible set of tests to benchmark AI coding assistant capabilities
4. Contribute to the ongoing discussion about the role of AI in software development

By replicating the Claude demo under various conditions, we aim to provide a more nuanced understanding of AI coding assistants' current capabilities and limitations.

## Problem Description

The original problem involves a Python function that resizes and crops images into circles. The initial implementation contains bugs that need to be fixed. Additionally, a test case is required to validate the function's correctness.

## Experiment Setup

We used four different system prompts to guide the AI coding assistant:

1. Original: The default system prompt
2. Expert: A prompt designed to elicit expert-level responses
3. Expert with Planning: Combines expert knowledge with a planning approach
4. Optimized Programmer: A merged and optimized version of the expert and planning prompts, incorporating prompt optimization techniques

For each prompt, we asked the AI to fix the cropping function and provide a test case.

## Experiments and Their Purposes

1. **Original Prompt**: Serves as a baseline to compare against enhanced prompts
2. **Expert Prompt**: Aims to leverage domain-specific knowledge for better code quality
3. **Expert with Planning Prompt**: Introduces a structured approach to problem-solving
4. **Optimized Programmer Prompt**: Attempts to combine the best aspects of expert knowledge and planning, with additional optimizations

## Detailed Analysis of System Prompts

This section compares the outputs of different system prompts against the original Claude demo outcomes.

### Original Claude Demo Outcomes

- Misidentified the actual bug
- Proposed an overcomplicated fix
- Wrote a test that didn't properly check for circular cropping
- Failed to provide a simple, effective solution

### Comparison of System Prompts

| Prompt Type          | Positives                                                                                                                                                                                     | Negatives                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Expert               | - Correctly identified and fixed transparency issue<br>- Provided comprehensive test case<br>- Included error handling                                                                        | - Slightly overcomplicated implementation                          |
| Optimized Programmer | - Conducted thorough code review<br>- Provided step-by-step planning approach<br>- Offered most comprehensive solution with error handling and input validation<br>- Created robust test case | None                                                               |
| Simple Planning      | - Correctly identified and fixed transparency issue<br>- Provided good test case<br>- Included instructions for further verification                                                          | - Lacked comprehensive error handling compared to other approaches |

### Analysis Summary

All three system prompts significantly outperformed the original Claude demo in terms of problem identification, solution quality, and testing.

1. **Expert Prompt**: Demonstrated accurate problem identification and comprehensive testing, but the implementation was slightly more complex than necessary.

2. **Optimized Programmer Prompt**: Proved to be the most effective approach, offering a thorough code review, step-by-step planning, and the most comprehensive solution with robust testing. No significant negatives were identified.

3. **Simple Planning Prompt**: Provided accurate problem identification and good testing, with clear instructions. However, it lacked the comprehensive error handling found in the other approaches.

The Optimized Programmer Prompt stands out as the most effective, addressing all aspects of the problem while providing valuable insights into the development process. Both the Expert Prompt and Simple Planning Prompt also offered substantial improvements over the original Claude demo, with only minor shortcomings compared to the Optimized Programmer approach.

This analysis demonstrates the significant impact that well-crafted system prompts can have on the performance of AI coding assistants, highlighting the potential for improved outcomes in software development tasks.

## Repository Structure

```code
.
├── expert_prompt_cropper/
│   ├── cropper.py
│   ├── cropper_test.py
│   ├── input_image.png
│   ├── output.md
│   └── system_prompt.md
├── optimized_programmer_prompt_cropper/
│   ├── cropper.py
│   ├── cropper_test.py
│   ├── input_image.png
│   ├── output.md
│   └── system_prompt.md
├── original/
│   ├── cropper.py
│   ├── input_image.png
│   └── output.md
├── simple_planning_prompt_cropper/
│   ├── cropper.py
│   ├── cropper_test.py
│   ├── input_image.png
│   ├── output.md
│   └── system_prompt.md
└── README.md
```

## How to Reproduce the Experiments

1. Clone this repository
2. Ensure you have Python and the required libraries (Pillow) installed
3. For each experiment:
   a. Navigate to the respective directory
   b. Review the `system_prompt.md` file
   c. Run the `cropper.py` script
   d. Check the output and generated images
   e. Run the `cropper_test.py` script (where available)
   f. Compare the results with the `output.md` file
