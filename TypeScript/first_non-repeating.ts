const string = 'aab'
const time = performance.now()

function NonRepeating(str: string) {
  const len = str.length
  for (let i = 0; i < len; i++) {
    const cur = str[i]
    const first = i === 0
    const last = i === len - 1
    const equalLeft = first || cur !== str[i - 1]
    const equalRight = last || cur !== str[i + 1]

    if (equalLeft && equalRight)
      return cur
    return ""
  }
}



const res = NonRepeating(string)
console.log({ res, time: performance.now() - time })

