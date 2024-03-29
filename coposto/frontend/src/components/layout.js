import React from "react";

import Footer from "./footer";
import Header from "./header";

export default class Layout extends React.Component {
  constructor() {
    super();
    this.state = {
      title: "Coposto",
    };
  }

  changeTitle(title) {
    this.setState({title});
  }

  render() {
    return (
      <div>
        <Header changeTitle={this.changeTitle.bind(this)} title={this.state.title} />
        <Footer />
      </div>
    );
  }
}