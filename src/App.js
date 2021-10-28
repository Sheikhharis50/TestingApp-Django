import React from 'react';
import makeTheme from './services/makeTheme';
import Header from './components/Headers';
import Footer from './components/Footers';

function App() {
  return (
    <React.Fragment>
      <Header />
      <main>

      </main>
      <Footer />
    </React.Fragment>
  );
}

export default makeTheme(App);


// import { getQuestions } from './api/questions';
// React.useEffect(() => {
  //   (async () => {
  //     console.log(await getQuestions());
  //   })()
  // });