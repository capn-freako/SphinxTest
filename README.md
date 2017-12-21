# SphinxTest
Simple test case for a Sphinx bug.

In order to observe the problem:

1. Clone this repository to your local working machine.
1. Move into the resultant directory ("SphinxTest", unless you specifically asked your `git clone` command for something else).
1. `git checkout aa2fa311`
1. `pushd doc/`
1. `make html`
1. Open *_build/index.html* in a browser.
1. Note that _cAtt_ equals '1'. This is correct.
1. `popd`
1. `git checkout master`
1. `pushd doc/`
1. `make html`
1. Open *_build/index.html* in a browser.
1. Note that _cAtt_ equals 'None'. This is incorrect.

Note the differences between aa2fa311 and HEAD:

`git diff aa2fa311`

```diff
diff --git a/sphinx_test_dbanas/sphinx_test_dbanas.py b/sphinx_test_dbanas/sphinx_test_dbanas.py
index 409d118..1c96a72 100644
--- a/sphinx_test_dbanas/sphinx_test_dbanas.py
+++ b/sphinx_test_dbanas/sphinx_test_dbanas.py
@@ -1,11 +1,12 @@
 """ A simple test case, illustrating a Sphinx bug. """

  import sys
  +from traits.api import HasTraits, Int

  -class SphinxTest(object):
  +class SphinxTest(HasTraits):
       """ Class docstring. """

       -    cAtt = int(1)  #: A class attribute.
       +    cAtt = Int(1)  #: A class attribute.

            def __init__(self):
                     """ Instance docstring. """
```

