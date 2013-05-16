# CodeSnippets

These are my Xcode 4 CodeSnippets.  
To use them, clone this repository into the following path:

    cd ~/Library/Developer/Xcode/UserData/CodeSnippets
    git clone git@github.com:jaydee3/CodeSnippets.git .

(The folder must be empty, to clone the repository directly in it.)  
And you're ready to go.

#### Installing the pre-commit hook  
This README is generated automatically using `.generateDescription.py`.  
To run this script automatically before each commit, install the pre-commit hook like this:

    sh .install-precommit-hook.sh

## Snippet Descriptions

**blockSafeSelfPointer.codesnippet**  (Block safe self pointer)  
Shortcut: `bs`  
A weak pointer to self (for usage in blocks).

    __weak typeof(self) blockSelf = self;

**createAndShowAUialertview.codesnippet**  (Create & show a UIAlertView)  
Shortcut: `alertview`  
Shows a newly created alertview

    UIAlertView* alertView = [[UIAlertView alloc] initWithTitle: <#title#>
                                                            message: <#message#>
                                                           delegate: <#self#>
                                                  cancelButtonTitle: <#nil#>
                                                  otherButtonTitles: <#@"OK"#>, nil];
        [alertView show];

**createAnImageview.codesnippet**  (Create an imageView)  
Shortcut: `iv`  
Inits a new imageView with an image via imageNamed.

    [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"<#imageName#>"]]

**createAReusableTablecell.codesnippet**  (Create a reusable TableCell)  
Shortcut: `tablecell`  
Initialises / deques a new cell from the tableview using an identifier

    // create / dequeue cell
    static NSString* identifier = @"<#identifier#>";
        UITableViewCell* cell = [tableView dequeueReusableCellWithIdentifier:identifier];
        if (cell == nil) {
            cell = [[<#UITableViewCell#> alloc] initWithStyle:<#UITableViewCellStyleSubtitle#> reuseIdentifier:identifier];
        }
        
        return cell;

**formattedString.codesnippet**  (Formatted String)  
Shortcut: `format`  
Shortcut for a formatted string

    [NSString stringWithFormat: @"<#string#>", <#param1#>]

**getDocumentsDirectory.codesnippet**  (Get Documents directory)  
Shortcut: `documents`  
Create path to documents directory

    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
        NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *filePath = [documentsDirectory stringByAppendingPathComponent:@"<#fileName#>"];

**importFramework.codesnippet**  (Import Framework)  
Shortcut: `imp2`  
import a framework

    #import <<#header#>>

**importHeader.codesnippet**  (Import header)  
Shortcut: `imp1`  
Import a header

    #import "<#header#>"

**incrementingForLoop.codesnippet**  (Incrementing For Loop)  
Shortcut: `fori`  
A For loop incrementing a local variable

    for (NSInteger i=0; i<<#count#>; i++) {
        <#statements#>
    }

**initalizeAnObject.codesnippet**  (Initalize an object)  
Shortcut: `alloc`  
creates a new object from a given class

    <#ClassName#> *<#variableName#> = [[<#ClassName#> alloc] init];

**keyValuePairForLocalization.codesnippet**  (Key-Value Pair for Localization)  
Shortcut: `key`  
A localization key and its value

    "<#keyName#>" = "<#value#>";

**localizeAString.codesnippet**  (Localize a string)  
Shortcut: `loca`  
Localizes a string from a given key

    NSLocalizedString(@"<#keyName#>", nil)

**pragmaMark.codesnippet**  (Pragma mark)  
Shortcut: `pragma`  
Add a new pragma mark

    #pragma mark <#comment#>

**pushAViewcontroller.codesnippet**  (Push a ViewController)  
Shortcut: `push`  
Pushes a newly created ViewController on the current NavigationController

    <#UIViewController#>* viewController = [[<#UIViewController#> alloc] init];
        [self.navigationController pushViewController:viewController animated:YES];

**setupAutoresizingOfAView.codesnippet**  (Setup autoresizing of a view)  
Shortcut: `autoresizing`  
Set the autoresizing flags of a view

    <#view#>.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;

