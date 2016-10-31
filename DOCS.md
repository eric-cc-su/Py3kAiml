#Documentation
***Oct. 31, 2016***

This documentation is meant to explain changes for v0.9+

v0.9 is still in progress. Currently in the middle of developing pattern matching for sets.

Other documentation:
- [AIML 2.0 Draft Specification](https://docs.google.com/document/d/1wNT25hJRyupcG51aO89UcQEiG-HkXRXusukADpFnDs4/pub)
- [AIML 2.0 Sets and Maps](https://docs.google.com/document/d/1DWHiOOcda58CflDZ0Wsm1CgP3Es6dpicb4MBbbpwzEk/pub)

## AIML Sets - PatternSet

One of the new features in AIML 2.0 is the ability to match inputs with sets of words and phrases.
The AIML syntax of AIML sets is as such:

`<category><pattern>...<set>*set_name*</set>...</pattern>...`

The `<set>` tag within the pattern does not allow attributes (unlike the `<set>` tags within the template). Instead, the
text within `<set>` represents the name of the set of words/phrases that the input should be matched against. This is
effectively a more specific `<star>` behavior that restricts possible matches to a certain set.

Within the codebase, the term **PatternSet** is used to represent an AIML set and **category** refers to the set that
should be matched against.

### Best Practices

- Sets should be written as `.set` files in Windows-style [INI format](Windows-style INI format) where the
section title is the set name. With this format, multiple sets can be contained within one .set file as the name of the
.set file is not used in constructing the set.
- The alternative, accepted formatting of `.set` files is to write the set as a list of lists. The first line should
be an opening bracket `[` and each line should be a list of the words in each phrase. **There should be no spaces. Each
word should be surrounded by quotation marks without any spaces**. **THE NAME OF THE SET FILE WILL BE THE NAME OF THE SET**


    file /path/to/foobar.set

    [
    ["foo"],
    ["bar"],
    ["foo", "bar"],
    ]

    BECOMES:

    {"foobar": ["foo", "bar", "foo bar"]}


- Sets should not share values. If a pattern matches more than one set (e.g. 'superheroes' and 'marvel'), only one set
will be considered when pattern matching.

#### Drawbacks
 - Does not yet support phrase matching, only word matching
