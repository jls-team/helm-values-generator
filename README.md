# helm-values-generator
Generates empty helm values from templates files.

Usage `python main.py <path to templates>`.

Dependencies - none.

Why? Needed quick script that goes thru templates directory and list all values templates to make development easer.

It only looks for `{{  }}` brackets and removes the filters. 

Less is more.


## Testing

It has one test, run by `python3 -m unittest`