# CodeSnippets

These are my Xcode CodeSnippets.  
To use them, clone this repository into the following path:  
(The folder must be empty, to clone the repository directly in it.)  

```sh
cd ~/Library/Developer/Xcode/UserData/CodeSnippets
git clone git@github.com:jaydee3/CodeSnippets.git .

```
And you're ready to go.

#### Installing the pre-commit hook  

This README is generated automatically using `.generateDescription.py`.  
To run this script automatically before each commit, install the pre-commit hook like this:

```sh
sh .install-precommit-hook.sh

```
## Snippet Descriptions

**Add a child ViewController**  
Adds a child ViewController to self

Shortcut: `childController`  
File: `objc_addAChildViewcontroller.codesnippet`  

```Obj-C
UIViewController *newController = <#newController#>;
    [newController willMoveToParentViewController:self];
    [self addChildViewController:newController];
    [self.contentView addSubview:newController.view];
    [newController didMoveToParentViewController:self];
```

**Create a reusable TableCell**  
Initialises / deques a new cell from the tableview using an identifier

Shortcut: `tablecell`  
File: `objc_createAReusableTablecell.codesnippet`  

```Obj-C
// create / dequeue cell
static NSString* identifier = @"<#identifier#>";
    UITableViewCell* cell = [tableView dequeueReusableCellWithIdentifier:identifier];
    if (cell == nil) {
        cell = [[<#UITableViewCell#> alloc] initWithStyle:<#UITableViewCellStyleSubtitle#> reuseIdentifier:identifier];
    }
    
    return cell;
```

**Create an imageView**  
Inits a new imageView with an image via imageNamed.

Shortcut: `iv`  
File: `objc_createAnImageview.codesnippet`  

```Obj-C
[[UIImageView alloc] initWithImage:[UIImage imageNamed:@"<#imageName#>"]]
```

**Create & show a UIAlertView**  
Shows a newly created alertview

Shortcut: `alertview`  
File: `objc_createAndShowAUialertview.codesnippet`  

```Obj-C
[[[UIAlertView alloc] initWithTitle:<#title#>
                            message:<#message#>
                           delegate:<#self#>
                  cancelButtonTitle:<#nil#>
                  otherButtonTitles:<#nil#>] show];
```

**Decrementing For Loop**  
A For Loop decrementing a local variable

Shortcut: `fori`  
File: `objc_decrementingForLoop.codesnippet`  

```Obj-C
for (NSInteger i=<#startValue#>; i><#count#>; i--) {
    <#statements#>
}
```

**Formatted String**  
Shortcut for a formatted string

Shortcut: `format`  
File: `objc_formattedString.codesnippet`  

```Obj-C
[NSString stringWithFormat:@"<#string#>", <#param1#>]
```

**Get Documents directory**  
Create path to documents directory

Shortcut: `documents`  
File: `objc_getDocumentsDirectory.codesnippet`  

```Obj-C
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = [paths objectAtIndex:0];
NSString *filePath = [documentsDirectory stringByAppendingPathComponent:@"<#fileName#>"];
```

**Import Framework**  
import a framework

Shortcut: `imp2`  
File: `objc_importFramework.codesnippet`  

```Obj-C
#import <<#header#>>
```

**Import header**  
Import a header

Shortcut: `imp1`  
File: `objc_importHeader.codesnippet`  

```Obj-C
#import "<#header#>"
```

**Incrementing For Loop**  
A For loop incrementing a local variable

Shortcut: `fori`  
File: `objc_incrementingForLoop.codesnippet`  

```Obj-C
for (NSInteger i=0; i<<#count#>; i++) {
    <#statements#>
}
```

**Initalize an object**  
creates a new object from a given class

Shortcut: `alloc`  
File: `objc_initalizeAnObject.codesnippet`  

```Obj-C
<#ClassName#> *<#variableName#> = [[<#ClassName#> alloc] init];
```

**Key-Value Pair for Localization**  
A localization key and its value

Shortcut: `key`  
File: `objc_keyValuePairForLocalization.codesnippet`  

```Obj-C
"<#keyName#>" = "<#value#>";
```

**Localize a string**  
Localizes a string from a given key

Shortcut: `loca`  
File: `objc_localizeAString.codesnippet`  

```Obj-C
NSLocalizedString(@"<#keyName#>", nil)
```

**Pragma mark**  
Add a new pragma mark

Shortcut: `pragma`  
File: `objc_pragmaMark.codesnippet`  

```Obj-C
#pragma mark <#comment#>
```

**Push a ViewController**  
Pushes a newly created ViewController on the current NavigationController

Shortcut: `push`  
File: `objc_pushAViewcontroller.codesnippet`  

```Obj-C
<#UIViewController#>* viewController = [[<#UIViewController#> alloc] init];
    [self.navigationController pushViewController:viewController animated:YES];
```

**Setup autoresizing of a view**  
Set the autoresizing flags of a view

Shortcut: `autoresizing`  
File: `objc_setupAutoresizingOfAView.codesnippet`  

```Obj-C
<#view#>.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
```

**singleton**  
A singleton implementation using dispatch_once

Shortcut: `singleton`  
File: `objc_singleton.codesnippet`  

```Obj-C
+ (instancetype)sharedInstance
{
  static id _sharedInstance = nil;
  static dispatch_once_t onceToken;
  dispatch_once(&onceToken, ^{
    _sharedInstance = [[self alloc] initSharedInstance];
  });
  return _sharedInstance;
}
```

**Strong self pointer**  
A strong pointer to self (for usage in blocks).

Shortcut: `ss`  
File: `objc_strongSelfPointer.codesnippet`  

```Obj-C
__strong __typeof(weakSelf) strongSelf = weakSelf;
```

**Weak self pointer**  
A weak pointer to self (for usage in blocks).

Shortcut: `ws`  
File: `objc_weakSelfPointer.codesnippet`  

```Obj-C
__weak __typeof(self) weakSelf = self;
```

**Guard Weak Self**  
Guard weak self to exist

Shortcut: `ws`  
File: `swift_guardWeakSelf.codesnippet`  

```Swift
guard let self = self else { return <#returnValue#> }
```

**Setup custom window & VC**  
Create window and rootVC

Shortcut: `setwin`  
File: `swift_setupCustomWindowAndVc.codesnippet`  

```Swift
window = UIWindow(windowScene: scene)
window?.rootViewController = UINavigationController(rootViewController: <#ViewController#>)
window?.makeKeyAndVisible()
```

