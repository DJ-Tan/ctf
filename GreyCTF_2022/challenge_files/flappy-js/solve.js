function atob(base64string) {
    return Buffer.from(base64string, 'base64').toString('utf-8')
}

var a = "AzhkZTRlYB0GDT0NAhItAQw4LR4DEzkABjkbAwM5DywDOCFlAhIfEgY5DwMDZgQiAxETNDZkGyYPEzEbAz4lDAIDDz4HZWAmAjsfPAc5Dw0DPx87MDkxAg8RBz4YEQMsAQMDAjQSAyQEAT5o";
a = atob(a);
var b = "";
for (var c in a) b += String.fromCharCode(85 ^ a.charCodeAt(c));
b = b.substring(0, b.indexOf("=") + 1), b = atob(b), b = atob(b), b = atob(b), b = atob(b), b = atob(b), b = atob(b)
console.log("grey{" + b + "}")