import './App.css';
import React from 'react';
import makeTheme, { ColorModeContext } from './services/makeTheme';
import Header from './components/Headers';
import Footer from './components/Footers';
import { useTheme } from '@mui/material/styles';
import IconButton from '@mui/material/IconButton';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';

function App() {
    const theme = useTheme();
    const colorMode = React.useContext(ColorModeContext);
    return (
        <React.Fragment>
            <Header />
            <main>
                {theme.palette.mode} mode
                <IconButton sx={{ ml: 1 }} onClick={colorMode.toggleColorMode} color="inherit">
                    {theme.palette.mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
                </IconButton>
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