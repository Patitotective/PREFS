"use strict";(self.webpackChunkprefs_docs=self.webpackChunkprefs_docs||[]).push([[942],{3905:function(e,n,t){t.d(n,{Zo:function(){return c},kt:function(){return f}});var r=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},i=Object.keys(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var o=r.createContext({}),p=function(e){var n=r.useContext(o),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},c=function(e){var n=p(e.components);return r.createElement(o.Provider,{value:n},e.children)},u={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,i=e.originalType,o=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),d=p(t),f=a,m=d["".concat(o,".").concat(f)]||d[f]||u[f]||i;return t?r.createElement(m,l(l({ref:n},c),{},{components:t})):r.createElement(m,l({ref:n},c))}));function f(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var i=t.length,l=new Array(i);l[0]=d;var s={};for(var o in n)hasOwnProperty.call(n,o)&&(s[o]=n[o]);s.originalType=e,s.mdxType="string"==typeof e?e:a,l[1]=s;for(var p=2;p<i;p++)l[p]=t[p];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},4515:function(e,n,t){t.r(n),t.d(n,{frontMatter:function(){return s},contentTitle:function(){return o},metadata:function(){return p},toc:function(){return c},default:function(){return d}});var r=t(7462),a=t(3366),i=(t(7294),t(3905)),l=["components"],s={id:"functions",title:"Functions",sidebar_position:3,hide_title:!0},o="Functions",p={unversionedId:"api/functions",id:"version-0.2.56/api/functions",isDocsHomePage:!1,title:"Functions",description:"*",source:"@site/versioned_docs/version-0.2.56/api/functions.md",sourceDirName:"api",slug:"/api/functions",permalink:"/PREFS/docs/0.2.56/api/functions",editUrl:"https://github.com/Patitotective/PREFS/tree/main/website/versioned_docs/version-0.2.56/api/functions.md",tags:[],version:"0.2.56",lastUpdatedBy:"Patitotective",lastUpdatedAt:1634483217,formattedLastUpdatedAt:"10/17/2021",sidebarPosition:3,frontMatter:{id:"functions",title:"Functions",sidebar_position:3,hide_title:!0},sidebar:"version-0.2.56/api",previous:{title:"Prefs class",permalink:"/PREFS/docs/0.2.56/api/prefs-class"},next:{title:"Command Line Interface",permalink:"/PREFS/docs/0.2.56/api/cli"}},c=[{value:"<code>convert_to_prefs()</code>",id:"convert_to_prefs",children:[],level:3},{value:"<code>read_prefs_file()</code>",id:"read_prefs_file",children:[],level:3},{value:"<code>read_json_file()</code>",id:"read_json_file",children:[],level:3},{value:"<code>read_yaml_file()</code>",id:"read_yaml_file",children:[],level:3}],u={toc:c};function d(e){var n=e.components,t=(0,a.Z)(e,l);return(0,i.kt)("wrapper",(0,r.Z)({},u,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"functions"},"Functions"),(0,i.kt)("hr",null),(0,i.kt)("h3",{id:"convert_to_prefs"},(0,i.kt)("inlineCode",{parentName:"h3"},"convert_to_prefs()")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"convert_to_prefs(*args, **kwargs) -> str\n")),(0,i.kt)("p",null,"Converts the given dictionary into PREFS format and returns it as string (similar to ",(0,i.kt)("inlineCode",{parentName:"p"},"dump")," function in ",(0,i.kt)("inlineCode",{parentName:"p"},"json"),"):"),(0,i.kt)("p",null,"Parameters:\n",(0,i.kt)("inlineCode",{parentName:"p"},"*args"),": This positional arguments will be passed to the ",(0,i.kt)("inlineCode",{parentName:"p"},"PREFS")," class.\n",(0,i.kt)("inlineCode",{parentName:"p"},"**kwargs"),": This keyword arguments will be passed to the ",(0,i.kt)("inlineCode",{parentName:"p"},"PREFS")," class."),(0,i.kt)("p",null,"Returns:\nA string with the given dictionary in PREFS format. "),(0,i.kt)("p",null,"Example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},'import PREFS\n\nprefs = {\n    "theme": "light",\n    "lang": "en",\n    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}\n}\n\nprefs_repr = PREFS.convert_to_prefs(prefs) # Converting the prefs dictionary into a string in PREFS format\n\nprint(prefs_repr) # Printing prefs_repr\n\n>>> \n#PREFS\ntheme=\'light\'\nlang=\'en\'\nkeybindings=>\n    Copy=\'Ctrl+C\'\n    Paste=\'Ctrl+V\'\n    Cut=\'Ctrl+X\'\n')),(0,i.kt)("p",null,"It can be used as an equivalent to ",(0,i.kt)("inlineCode",{parentName:"p"},"dump")," function in JSON."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},'import PREFS\n\nprefs = {\n    "theme": "light",\n    "lang": "en",\n    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}\n}\n\nwith open("settings.prefs", "w+") as file:\n    file.write(PREFS.convert_to_prefs(prefs))\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py",metastring:'title="settings.prefs"',title:'"settings.prefs"'},"#PREFS\ntheme='light'\nlang='en'\nkeybindings=>\n    Copy='Ctrl+C'\n    Paste='Ctrl+V'\n    Cut='Ctrl+X'\n")),(0,i.kt)("h3",{id:"read_prefs_file"},(0,i.kt)("inlineCode",{parentName:"h3"},"read_prefs_file()")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"read_prefs_file(filename: str, **kwargs) -> dict\n")),(0,i.kt)("p",null,"Return the value of PREFS file given it's filename."),(0,i.kt)("p",null,"Parameters:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"**kwargs"),": This keyword arguments will be used to create a ",(0,i.kt)("inlineCode",{parentName:"li"},"PREFS")," instance.")),(0,i.kt)("p",null,"Returns:\nA dictionary with the PREFS of the given PREFS filename."),(0,i.kt)("p",null,"Example:",(0,i.kt)("br",{parentName:"p"}),"\n","If we have a file like this:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="prefs.prefs"',title:'"prefs.prefs"'},"#PREFS\ntheme='light'\nlang='en' # Supports comments\n")),(0,i.kt)("p",null,"We can read it this way:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},'import PREFS\n\n# Instead of doing this\n"""\nuser_prefs = PREFS.Prefs(prefs={\n    "theme": "light",\n    "lang": "en"\n    })\n"""\n\nuser_prefs = PREFS.Prefs(PREFS.read_prefs_file("prefs.prefs"))\n\nprint(user_prefs.file)\n\n>>> {\'theme\': \'light\', \'lang\': \'en\'}\n')),(0,i.kt)("div",{className:"admonition admonition-tip alert alert--success"},(0,i.kt)("div",{parentName:"div",className:"admonition-heading"},(0,i.kt)("h5",{parentName:"div"},(0,i.kt)("span",{parentName:"h5",className:"admonition-icon"},(0,i.kt)("svg",{parentName:"span",xmlns:"http://www.w3.org/2000/svg",width:"12",height:"16",viewBox:"0 0 12 16"},(0,i.kt)("path",{parentName:"svg",fillRule:"evenodd",d:"M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z"}))),"TIP")),(0,i.kt)("div",{parentName:"div",className:"admonition-content"},(0,i.kt)("p",{parentName:"div"},"Remember to write quotes around all the strings."))),(0,i.kt)("h3",{id:"read_json_file"},(0,i.kt)("inlineCode",{parentName:"h3"},"read_json_file()")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"read_json_file(filename: str, **kwargs) -> dict\n")),(0,i.kt)("p",null,"Reads a JSON file and returns it's value."),(0,i.kt)("p",null,"Parameters:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"filename (str)"),": The name of JSON file to read (path)."),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"**kwargs"),": This keyword arguments will be passed to the ",(0,i.kt)("inlineCode",{parentName:"li"},"json.load")," function.")),(0,i.kt)("p",null,"Example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},'import PREFS\n\njson_content = PREFS.read_json_file("filename.json") # Read filename.json" and store it\'s value in prefs\nuser_prefs = PREFS.Prefs(json_content) # Create an instance of the PREFS class using a json file as input for the prefs argument\n')),(0,i.kt)("h3",{id:"read_yaml_file"},(0,i.kt)("inlineCode",{parentName:"h3"},"read_yaml_file()")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"read_yaml_file(filename: str, **kwargs) -> dict\n")),(0,i.kt)("p",null,"Reads a YAML file and returns it's value."),(0,i.kt)("p",null,"Parameters:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"filename (str)"),": The name of YAML file to read (path).")),(0,i.kt)("p",null,"Example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},'import PREFS\n\nyaml_content = PREFS.read_yaml_file("filename.yaml") # Read filename.yaml and store it\'s value in prefs\nuser_prefs = PREFS.Prefs(yaml_content) # Create an instance of the PREFS class using a yaml file as input for the prefs argument\n')))}d.isMDXComponent=!0}}]);