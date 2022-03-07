## Regex
* `\w+…(?:.+)` - Match anything past (the https://t.co/ link) … any incomplete words
* `…(?:.+)` - Match any `… https://t.co/` lines that don't have spaces before it
* `@\w+\s` - Match any line that starts with `@username `
* `\shttps:\/\/t.co\/.+$` - Matches any errant `https://t.co` domains, indicating images and tweets
* `https:\/\/t.co\/.+$` Matches any `https://t.co` domains on their own
* `&\w+;` - Match any HTML entites for manual changing
* `^(?:[\t ]*(?:\r?\n|\r))+` - Match any newline (Disclaimer: not my regex)