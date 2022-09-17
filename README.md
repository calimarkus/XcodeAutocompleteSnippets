# CodeSnippets

These are my Xcode CodeSnippets.  
To use them, clone this repository into the following path:  
(The folder must be empty, to clone the repository directly in it.)  

    cd ~/Library/Developer/Xcode/UserData/CodeSnippets
    git clone git@github.com:jaydee3/CodeSnippets.git .

And you're ready to go.

#### Installing the pre-commit hook  

This README is generated automatically using `.generateDescription.py`.  
To run this script automatically before each commit, install the pre-commit hook like this:

    sh .install-precommit-hook.sh

## Snippet Descriptions

**objc_addAChildViewcontroller.codesnippet**  (Add a child ViewController)  
Language: `Obj-C`  
Shortcut: `childController`  
Adds a child ViewController to self

    UIViewController *newController = <#newController#>;
        [newController willMoveToParentViewController:self];
        [self addChildViewController:newController];
        [self.contentView addSubview:newController.view];
        [newController didMoveToParentViewController:self];

**objc_createAReusableTablecell.codesnippet**  (Create a reusable TableCell)  
Language: `Obj-C`  
Shortcut: `tablecell`  
Initialises / deques a new cell from the tableview using an identifier

    // create / dequeue cell
    static NSString* identifier = @"<#identifier#>";
        UITableViewCell* cell = [tableView dequeueReusableCellWithIdentifier:identifier];
        if (cell == nil) {
            cell = [[<#UITableViewCell#> alloc] initWithStyle:<#UITableViewCellStyleSubtitle#> reuseIdentifier:identifier];
        }
        
        return cell;

**objc_createAnImageview.codesnippet**  (Create an imageView)  
Language: `Obj-C`  
Shortcut: `iv`  
Inits a new imageView with an image via imageNamed.

    [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"<#imageName#>"]]

**objc_createAndShowAUialertview.codesnippet**  (Create & show a UIAlertView)  
Language: `Obj-C`  
Shortcut: `alertview`  
Shows a newly created alertview

    [[[UIAlertView alloc] initWithTitle:<#title#>
                                message:<#message#>
                               delegate:<#self#>
                      cancelButtonTitle:<#nil#>
                      otherButtonTitles:<#nil#>] show];

**objc_decrementingForLoop.codesnippet**  (Decrementing For Loop)  
Language: `Obj-C`  
Shortcut: `fori`  
A For Loop decrementing a local variable

    for (NSInteger i=<#startValue#>; i><#count#>; i--) {
        <#statements#>
    }

**objc_formattedString.codesnippet**  (Formatted String)  
Language: `Obj-C`  
Shortcut: `format`  
Shortcut for a formatted string

    [NSString stringWithFormat:@"<#string#>", <#param1#>]

**objc_getDocumentsDirectory.codesnippet**  (Get Documents directory)  
Language: `Obj-C`  
Shortcut: `documents`  
Create path to documents directory

    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
        NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *filePath = [documentsDirectory stringByAppendingPathComponent:@"<#fileName#>"];

**objc_importFramework.codesnippet**  (Import Framework)  
Language: `Obj-C`  
Shortcut: `imp2`  
import a framework

    #import <<#header#>>

**objc_importHeader.codesnippet**  (Import header)  
Language: `Obj-C`  
Shortcut: `imp1`  
Import a header

    #import "<#header#>"

**objc_incrementingForLoop.codesnippet**  (Incrementing For Loop)  
Language: `Obj-C`  
Shortcut: `fori`  
A For loop incrementing a local variable

    for (NSInteger i=0; i<<#count#>; i++) {
        <#statements#>
    }

**objc_initalizeAnObject.codesnippet**  (Initalize an object)  
Language: `Obj-C`  
Shortcut: `alloc`  
creates a new object from a given class

    <#ClassName#> *<#variableName#> = [[<#ClassName#> alloc] init];

**objc_keyValuePairForLocalization.codesnippet**  (Key-Value Pair for Localization)  
Language: `Obj-C`  
Shortcut: `key`  
A localization key and its value

    "<#keyName#>" = "<#value#>";

**objc_localizeAString.codesnippet**  (Localize a string)  
Language: `Obj-C`  
Shortcut: `loca`  
Localizes a string from a given key

    NSLocalizedString(@"<#keyName#>", nil)

**objc_pragmaMark.codesnippet**  (Pragma mark)  
Language: `Obj-C`  
Shortcut: `pragma`  
Add a new pragma mark

    #pragma mark <#comment#>

**objc_pushAViewcontroller.codesnippet**  (Push a ViewController)  
Language: `Obj-C`  
Shortcut: `push`  
Pushes a newly created ViewController on the current NavigationController

    <#UIViewController#>* viewController = [[<#UIViewController#> alloc] init];
        [self.navigationController pushViewController:viewController animated:YES];

**objc_setupAutoresizingOfAView.codesnippet**  (Setup autoresizing of a view)  
Language: `Obj-C`  
Shortcut: `autoresizing`  
Set the autoresizing flags of a view

    <#view#>.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;

**objc_singleton.codesnippet**  (singleton)  
Language: `Obj-C`  
Shortcut: `singleton`  
A singleton implementation using dispatch_once

    + (instancetype)sharedInstance
    {
      static id _sharedInstance = nil;
      static dispatch_once_t onceToken;
      dispatch_once(&onceToken, ^{
        _sharedInstance = [[self alloc] initSharedInstance];
      });
      return _sharedInstance;
    }

**objc_strongSelfPointer.codesnippet**  (Strong self pointer)  
Language: `Obj-C`  
Shortcut: `ss`  
A strong pointer to self (for usage in blocks).

    __strong __typeof(weakSelf) strongSelf = weakSelf;

**objc_weakSelfPointer.codesnippet**  (Weak self pointer)  
Language: `Obj-C`  
Shortcut: `ws`  
A weak pointer to self (for usage in blocks).

    __weak __typeof(self) weakSelf = self;

**swift_guardWeakSelf.codesnippet**  (Guard Weak Self)  
Language: `Swift`  
Shortcut: `ws`  
Guard weak self to exist

    guard let self = self else { return <#returnValue#> }

**swift_setupCustomWindowAndVc.codesnippet**  (Setup custom window & VC)  
Language: `Swift`  
Shortcut: `setwin`  
Create window and rootVC

    window = UIWindow(windowScene: scene)
    window?.rootViewController = UINavigationController(rootViewController: <#ViewController#>)
    window?.makeKeyAndVisible()

