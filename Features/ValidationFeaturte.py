Feature: Ensure
Correct
API
Endpoint
Schema
Configuration

Scenario: Validate
that
the
API
response
matches
the
expected
JSON
schema

Given
I
have
the
API
endpoint
"https://api.example.com/data"

When
I
send
a
GET
request
to
the
endpoint

Then
the
response
should
match
the
expected
JSON
schema

And
print
the
result in the
test
report

