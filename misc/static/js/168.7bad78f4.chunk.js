(this.webpackJsonpmizaweb2=this.webpackJsonpmizaweb2||[]).push([[168],{247:function(e,n,a){var t=a(20),i=a(64);function c(e){return e?"string"===typeof e?e:e.source:null}function u(e){return r("(?=",e,")")}function r(){for(var e=arguments.length,n=new Array(e),a=0;a<e;a++)n[a]=arguments[a];var t=n.map((function(e){return c(e)})).join("");return t}function o(e){var n=e[e.length-1];return"object"===typeof n&&n.constructor===Object?(e.splice(e.length-1,1),n):{}}function s(){for(var e=arguments.length,n=new Array(e),a=0;a<e;a++)n[a]=arguments[a];var t=o(n),i="("+(t.capture?"":"?:")+n.map((function(e){return c(e)})).join("|")+")";return i}var l=function(e){return r(/\b/,e,/\w$/.test(e)?/\b/:/\B/)},p=["Protocol","Type"].map(l),m=["init","self"].map(l),d=["Any","Self"],F=["actor","associatedtype","async","await",/as\?/,/as!/,"as","break","case","catch","class","continue","convenience","default","defer","deinit","didSet","do","dynamic","else","enum","extension","fallthrough",/fileprivate\(set\)/,"fileprivate","final","for","func","get","guard","if","import","indirect","infix",/init\?/,/init!/,"inout",/internal\(set\)/,"internal","in","is","lazy","let","mutating","nonmutating",/open\(set\)/,"open","operator","optional","override","postfix","precedencegroup","prefix",/private\(set\)/,"private","protocol",/public\(set\)/,"public","repeat","required","rethrows","return","set","some","static","struct","subscript","super","switch","throws","throw",/try\?/,/try!/,"try","typealias",/unowned\(safe\)/,/unowned\(unsafe\)/,"unowned","var","weak","where","while","willSet"],f=["false","nil","true"],h=["assignment","associativity","higherThan","left","lowerThan","none","right"],b=["#colorLiteral","#column","#dsohandle","#else","#elseif","#endif","#error","#file","#fileID","#fileLiteral","#filePath","#function","#if","#imageLiteral","#keyPath","#line","#selector","#sourceLocation","#warn_unqualified_access","#warning"],v=["abs","all","any","assert","assertionFailure","debugPrint","dump","fatalError","getVaList","isKnownUniquelyReferenced","max","min","numericCast","pointwiseMax","pointwiseMin","precondition","preconditionFailure","print","readLine","repeatElement","sequence","stride","swap","swift_unboxFromSwiftValueWithType","transcode","type","unsafeBitCast","unsafeDowncast","withExtendedLifetime","withUnsafeMutablePointer","withUnsafePointer","withVaList","withoutActuallyEscaping","zip"],w=s(/[/=\-+!*%<>&|^~?]/,/[\u00A1-\u00A7]/,/[\u00A9\u00AB]/,/[\u00AC\u00AE]/,/[\u00B0\u00B1]/,/[\u00B6\u00BB\u00BF\u00D7\u00F7]/,/[\u2016-\u2017]/,/[\u2020-\u2027]/,/[\u2030-\u203E]/,/[\u2041-\u2053]/,/[\u2055-\u205E]/,/[\u2190-\u23FF]/,/[\u2500-\u2775]/,/[\u2794-\u2BFF]/,/[\u2E00-\u2E7F]/,/[\u3001-\u3003]/,/[\u3008-\u3020]/,/[\u3030]/),y=s(w,/[\u0300-\u036F]/,/[\u1DC0-\u1DFF]/,/[\u20D0-\u20FF]/,/[\uFE00-\uFE0F]/,/[\uFE20-\uFE2F]/),g=r(w,y,"*"),E=s(/[a-zA-Z_]/,/[\u00A8\u00AA\u00AD\u00AF\u00B2-\u00B5\u00B7-\u00BA]/,/[\u00BC-\u00BE\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF]/,/[\u0100-\u02FF\u0370-\u167F\u1681-\u180D\u180F-\u1DBF]/,/[\u1E00-\u1FFF]/,/[\u200B-\u200D\u202A-\u202E\u203F-\u2040\u2054\u2060-\u206F]/,/[\u2070-\u20CF\u2100-\u218F\u2460-\u24FF\u2776-\u2793]/,/[\u2C00-\u2DFF\u2E80-\u2FFF]/,/[\u3004-\u3007\u3021-\u302F\u3031-\u303F\u3040-\uD7FF]/,/[\uF900-\uFD3D\uFD40-\uFDCF\uFDF0-\uFE1F\uFE30-\uFE44]/,/[\uFE47-\uFEFE\uFF00-\uFFFD]/),A=s(E,/\d/,/[\u0300-\u036F\u1DC0-\u1DFF\u20D0-\u20FF\uFE20-\uFE2F]/),N=r(E,A,"*"),C=r(/[A-Z]/,A,"*"),k=["autoclosure",r(/convention\(/,s("swift","block","c"),/\)/),"discardableResult","dynamicCallable","dynamicMemberLookup","escaping","frozen","GKInspectable","IBAction","IBDesignable","IBInspectable","IBOutlet","IBSegueAction","inlinable","main","nonobjc","NSApplicationMain","NSCopying","NSManaged",r(/objc\(/,N,/\)/),"objc","objcMembers","propertyWrapper","requires_stored_property_inits","resultBuilder","testable","UIApplicationMain","unknown","usableFromInline"],D=["iOS","iOSApplicationExtension","macOS","macOSApplicationExtension","macCatalyst","macCatalystApplicationExtension","watchOS","watchOSApplicationExtension","tvOS","tvOSApplicationExtension","swift"];e.exports=function(e){var n={match:/\s+/,relevance:0},a=e.COMMENT("/\\*","\\*/",{contains:["self"]}),c=[e.C_LINE_COMMENT_MODE,a],o={match:[/\./,s.apply(void 0,i(p).concat(i(m)))],className:{2:"keyword"}},w={match:r(/\./,s.apply(void 0,F)),relevance:0},E=F.filter((function(e){return"string"===typeof e})).concat(["_|0"]),B=F.filter((function(e){return"string"!==typeof e})).concat(d).map(l),_={variants:[{className:"keyword",match:s.apply(void 0,i(B).concat(i(m)))}]},S={$pattern:s(/\b\w+/,/#\w+/),keyword:E.concat(b),literal:f},M=[o,w,_],x=[{match:r(/\./,s.apply(void 0,v)),relevance:0},{className:"built_in",match:r(/\b/,s.apply(void 0,v),/(?=\()/)}],I={match:/->/,relevance:0},O=[I,{className:"operator",relevance:0,variants:[{match:g},{match:"\\.(\\.|".concat(y,")+")}]}],L="([0-9]_*)+",T="([0-9a-fA-F]_*)+",P={className:"number",relevance:0,variants:[{match:"\\b(".concat(L,")(\\.(").concat(L,"))?")+"([eE][+-]?(".concat(L,"))?\\b")},{match:"\\b0x(".concat(T,")(\\.(").concat(T,"))?")+"([pP][+-]?(".concat(L,"))?\\b")},{match:/\b0o([0-7]_*)+\b/},{match:/\b0b([01]_*)+\b/}]},j=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return{className:"subst",variants:[{match:r(/\\/,e,/[0\\tnr"']/)},{match:r(/\\/,e,/u\{[0-9a-fA-F]{1,8}\}/)}]}},z=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return{className:"subst",match:r(/\\/,e,/[\t ]*(?:[\r\n]|\r\n)/)}},K=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return{className:"subst",label:"interpol",begin:r(/\\/,e,/\(/),end:/\)/}},$=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return{begin:r(e,/"""/),end:r(/"""/,e),contains:[j(e),z(e),K(e)]}},q=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return{begin:r(e,/"/),end:r(/"/,e),contains:[j(e),K(e)]}},U={className:"string",variants:[$(),$("#"),$("##"),$("###"),q(),q("#"),q("##"),q("###")]},Z={match:r(/`/,N,/`/)},V=[Z,{className:"variable",match:/\$\d+/},{className:"variable",match:"\\$".concat(A,"+")}],W=[{match:/(@|#)available/,className:"keyword",starts:{contains:[{begin:/\(/,end:/\)/,keywords:D,contains:[].concat(O,[P,U])}]}},{className:"keyword",match:r(/@/,s.apply(void 0,k))},{className:"meta",match:r(/@/,N)}],G={match:u(/\b[A-Z]/),relevance:0,contains:[{className:"type",match:r(/(AV|CA|CF|CG|CI|CL|CM|CN|CT|MK|MP|MTK|MTL|NS|SCN|SK|UI|WK|XC)/,A,"+")},{className:"type",match:C,relevance:0},{match:/[?!]+/,relevance:0},{match:/\.\.\./,relevance:0},{match:r(/\s+&\s+/,u(C)),relevance:0}]},J={begin:/</,end:/>/,keywords:S,contains:[].concat(c,M,W,[I,G])};G.contains.push(J);var R,X={begin:/\(/,end:/\)/,relevance:0,keywords:S,contains:["self",{match:r(N,/\s*:/),keywords:"_|0",relevance:0}].concat(c,M,x,O,[P,U],V,W,[G])},H={begin:/</,end:/>/,contains:[].concat(c,[G])},Q={begin:/\(/,end:/\)/,keywords:S,contains:[{begin:s(u(r(N,/\s*:/)),u(r(N,/\s+/,N,/\s*:/))),end:/:/,relevance:0,contains:[{className:"keyword",match:/\b_\b/},{className:"params",match:N}]}].concat(c,M,O,[P,U],W,[G,X]),endsParent:!0,illegal:/["']/},Y={match:[/func/,/\s+/,s(Z.match,N,g)],className:{1:"keyword",3:"title.function"},contains:[H,Q,n],illegal:[/\[/,/%/]},ee={match:[/\b(?:subscript|init[?!]?)/,/\s*(?=[<(])/],className:{1:"keyword"},contains:[H,Q,n],illegal:/\[|%/},ne={match:[/operator/,/\s+/,g],className:{1:"keyword",3:"title"}},ae={begin:[/precedencegroup/,/\s+/,C],className:{1:"keyword",3:"title"},contains:[G],keywords:[].concat(h,f),end:/}/},te=t(U.variants);try{for(te.s();!(R=te.n()).done;){var ie=R.value.contains.find((function(e){return"interpol"===e.label}));ie.keywords=S;var ce=[].concat(M,x,O,[P,U],V);ie.contains=[].concat(i(ce),[{begin:/\(/,end:/\)/,contains:["self"].concat(i(ce))}])}}catch(ue){te.e(ue)}finally{te.f()}return{name:"Swift",keywords:S,contains:[].concat(c,[Y,ee,{beginKeywords:"struct protocol class extension enum actor",end:"\\{",excludeEnd:!0,keywords:S,contains:[e.inherit(e.TITLE_MODE,{className:"title.class",begin:/[A-Za-z$_][\u00C0-\u02B80-9A-Za-z$_]*/})].concat(M)},ne,ae,{beginKeywords:"import",end:/$/,contains:[].concat(c),relevance:0}],M,x,O,[P,U],V,W,[G,X])}}}}]);
//# sourceMappingURL=168.7bad78f4.chunk.js.map