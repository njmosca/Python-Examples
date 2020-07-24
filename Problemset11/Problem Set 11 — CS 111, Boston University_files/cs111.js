/*
 * cs111.js
 */

var MIN_WIDTH = 1220
var MIN_SCROLL_AMOUNT = 100 // how much to scroll before "back to top" appears

var PYTHON_TUTOR_LINKS = true

var rightDIV                // element of #right on page
var rightTOC                // element of TOC in #right

var doRightTOC = false

var showing = false             // whether #right is showing
var showingBackToTop = false

var initialHeaderLocation
var initialHeaderHTML
var initialHeaderBackgroundColor

var headingElements = []    // heading elements on the page
var anchorElements = []     // anchors in right TOC to the headings

var currentHeading = -1     // (index into headings array)


function setup() {
    if (isMobile(navigator.userAgent || navigator.vendor || window.opera))
        return

    var headerElement = document.getElementById('header')
    initialHeaderLocation = headerElement.href
    initialHeaderHTML = headerElement.innerHTML

    var matches = document.getElementsByClassName('toc')

    if (matches.length == 1)
        setupTOC(matches[0])

    // still schedule scroll() because it also handles "back to top" button
    window.setInterval(scroll, 500)

    if (PYTHON_TUTOR_LINKS)
        setupTutorLinks()

}

function setupTutorLinks() {
    // attach Python Tutor links to code block <div>s
    var codeBlocks = document.getElementsByClassName('codehilite')

    for (var i = 0; i < codeBlocks.length; i++) {
        // skip this block if it isn't a Python block
        if (codeBlocks[i].className.indexOf('python') < 0)
            continue

        // skip this block if it doesn't have a child
        if (!codeBlocks[i].hasChildNodes())
            continue

        var child = codeBlocks[i].childNodes[0]

        // skip this block if its child is not a <pre>
        if (child.tagName != 'PRE')
            continue

        // skip this block if it's too simple
        if (numUsefulLines(child.textContent) < 2)
            continue

        var code = ''

        // if this block's <pre> contains the Python prompt ('>>>'),
        // convert those lines of code to print()s
        if (containsPrompts(child.textContent))
            code = promptLinesToPrints(child.textContent)
        else
            code = child.textContent

        // build link
        var url = 'http://pythontutor.com/visualize.html#py=3&code='
        url += encodeURIComponent(code)

        // attach link as child of <div>
        var hyperlink = document.createElement('A')
        hyperlink.href = url
        hyperlink.target = '_blank'
        hyperlink.textContent = 'Open in Python Tutor'
        hyperlink.className += 'pythontutor'

        codeBlocks[i].appendChild(hyperlink)
    }
}

function setupTOC(tocElement) {
    // enable and set up floating TOC
    doRightTOC = true

    rightDIV = document.getElementById('right')
    rightTOC = tocElement.cloneNode(true)
    rightDIV.appendChild(rightTOC)

    var topUL = rightTOC.children[0].children
    for (var i = 0; i < topUL.length; i++) {
        var li = topUL[i]

        for (var j = 0; j < li.children.length; j++) {
            if (li.children[j].tagName == "A") {
                addAnchor(li.children[j])
            } else if (li.children[j].tagName == "UL") {
                var subUL = li.children[j].children

                for (var k = 0; k < subUL.length; k++) {
                    var subLI = subUL[k]

                    for (var m = 0; m < subLI.children.length; m++) {
                        if (subLI.children[m].tagName == "A") {
                            addAnchor(subLI.children[m])

                        } else if (subLI.children[m].tagName == "UL") {
                            var subSubUL = subLI.children[m].children

                            for (var n = 0; n < subSubUL.length; n++) {
                                var subSubLI = subSubUL[n]

                                for (var p = 0; p < subSubLI.children.length; p++)
                                    if (subSubLI.children[p].tagName == "A")
                                        addAnchor(subSubLI.children[p])

                            }
                        }
                    }
                }
            }
        }
    }
}

// adds an anchor that links to a heading to the global array
function addAnchor(anchor) {
    anchorElements.push(anchor)

    var href = anchor.getAttribute('href')
    var hrefID = href.substring(1, href.length)
    var el = document.getElementById(hrefID)

    headingElements.push(el)
}

function getScrollAmount() {
    return Math.max(document.documentElement.scrollTop,
                    document.body.scrollTop)
}

function scroll() {
    if (!showingBackToTop && getScrollAmount() > MIN_SCROLL_AMOUNT) {
        showBackToTop()
        showingBackToTop = true
    }

    if (showingBackToTop && getScrollAmount() < MIN_SCROLL_AMOUNT) {
        hideBackToTop()
        showingBackToTop = false
    }

    if (doRightTOC) {
        if (!showing && window.innerWidth > MIN_WIDTH) {
            showRightTOC()
            showing = true
        }

        if (showing && window.innerWidth < MIN_WIDTH) {
            hideRightTOC()
            showing = false
        }

        // update which heading we show in the TOC
        var h = calculateHeading()
        if (h != currentHeading) {
            changeHeading(h)
        }
    }
}

function showRightTOC() {
    // show #right
    rightDIV.style.display = 'inherit'

    // hide the TOC inline in #middle
    var matches = document.getElementsByClassName('toc')
    for (var i = 0; i < matches.length; i++)
        if (matches[i] != rightTOC)
            matches[i].style.display = 'none'
}

function hideRightTOC() {
    // un-hide the TOC inline in #middle
    var matches = document.getElementsByClassName('toc')
    for (var i = 0; i < matches.length; i++)
        if (matches[i] != rightTOC)
            matches[i].style.display = 'inherit'

    // hide #right
    rightDIV.style.display = 'none'
}

function showBackToTop() {
    var el = document.getElementById('header')
    el.innerHTML = '&uarr;'
    el.className = 'backtotop'
    el.href = '#'
    el.onclick = function() {
        window.scrollTo(0, 0)
    }
}

function hideBackToTop() {
    var el = document.getElementById('header')
    el.className = ''
    el.innerHTML = initialHeaderHTML
    el.href = initialHeaderLocation
    el.style.backgroundColor = initialHeaderBackgroundColor
}

function calculateHeading() {
    var closest = 0
    var cr
    for (var i = 0; i < headingElements.length; i++) {
        cr = headingElements[i].getBoundingClientRect()

        if (cr.top - 120 >= 0) {
            break
        } else {
            closest = i
        }
    }

    return closest
}

function changeHeading(newIndex) {
    if (currentHeading >= 0)
        anchorElements[currentHeading].className = ''

    anchorElements[newIndex].className = 'current'

    currentHeading = newIndex
}

function startsWith(str, prefix) {
    if (str.length < prefix)
        return false

    for (var i = 0; i < prefix.length; i++)
        if (str[i] != prefix[i])
            return false

    return true
}

function numUsefulLines(str) {
    var lines = str.split('\n')
    var numUseful = 0
    for (var i = 0; i < lines.length; i++)
        if (lines[i].length > 0)
            numUseful++

    return numUseful
}

function containsPrompts(code) {
    var lines = code.split('\n')
    for (var i = 0; i < lines.length; i++)
        if (startsWith(lines[i].trim(), '>>>'))
            return true

    return false
}

function isAssignment(stmt) {
    var re = /\s*=\s*/
    return re.test(stmt)
}

function introducesIndent(stmt) {
    var re = /:\s*$/
    return re.test(stmt)
}

function encloseInPrint(stmt) {
    var i = stmt.indexOf('#')

    if (i < 0) {
        return 'print(' + stmt + ')'
    } else {
        var withoutComment = stmt.substring(0, i).trim()
        var restOfLine = stmt.substring(withoutComment.length)
        return 'print(' + withoutComment + ')' + restOfLine
    }
}

function promptLinesToPrints(code) {
    var lines = code.split('\n')
    var transformedLines = []
    for (var i = 0; i < lines.length; i++) {
        // copy comments verbatim
        if (startsWith(lines[i].trim(), '#')) {
            transformedLines.push(lines[i])
            continue
        }

        var start = lines[i].indexOf('>>>')
        if (start == 0) {
            // remove the prompt characters from this line
            var statement = lines[i].substring(3).trim()

            if (!isAssignment(statement) && !introducesIndent(statement))
                statement = encloseInPrint(statement)

            transformedLines.push(statement)

        } else {
            // if the tokens on this line are indented, we assume that
            // they are part of a function body defined on the Shell
            // or a multi-line statement, so we include them
            if (lines[i][0] == ' ') {
                transformedLines.push(lines[i])
                continue
            }

            // otherwise, we assume this line represents the output of
            // the Shell in the transcript, which we don't want to send
            // to the tutor
        }
    }

    return transformedLines.join('\n')
}

function isMobile(a) {return (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|(o|a)d)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))}

