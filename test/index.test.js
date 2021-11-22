const fs = require("fs");
const path = require("path");
const chai = require("chai");
const CSSOM = require("cssom");
chai.use(require("chai-dom"));
const { expect } = chai;

const cssFile = fs.readFileSync(
  path.resolve(__dirname, "../css/style.css"),
  "utf-8"
);

function findRule(rules, cssSelector) {
  return rules.find((r) => r.selectorText === cssSelector);
}

describe("css/style.css", () => {
  let css;
  before(() => {
    css = CSSOM.parse(cssFile);
  });

  it("corrects the 'body' background declaration", () => {
    const rule = findRule(css.cssRules, "body");
    const hint = "Incorrect background property for body";
    expect(rule.style["background"], hint).to.eq("pink");
  });

  it("corrects the 'h1' font-size declaration", () => {
    const rule = findRule(css.cssRules, "h1");
    const hint = "Incorrect font-size property for h1";
    expect(rule.style["font-size"], hint).to.eq("3em");
  });

  it("corrects the 'h2' font-weight declaration", () => {
    const rule = findRule(css.cssRules, "h2");
    const hint = "Incorrect font-weight property for h2";
    expect(rule.style["font-weight"], hint).to.eq("normal");
  });

  it("corrects the '.completed' font-size declaration", () => {
    const rule = findRule(css.cssRules, ".completed");
    const hint = "Incorrect font-size property for .completed";
    expect(rule.style["font-size"], hint).to.eq("12px");
  });

  it("corrects the '#tasks .completed' background declaration", () => {
    const rule = findRule(css.cssRules, "#tasks .completed");
    const hint = "Incorrect background property for '#tasks .completed'";
    expect(rule.style["background"], hint).to.eq("#ccc");
  });
});
