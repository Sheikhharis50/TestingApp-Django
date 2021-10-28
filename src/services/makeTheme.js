import { red } from '@mui/material/colors';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import React from 'react';

export const ColorModeContext = React.createContext({ toggleColorMode: () => { } });

const makeTheme = (Component) => {
    return (props) => {
        const [mode, setMode] = React.useState('light');
        const colorMode = React.useMemo(
            () => ({
                toggleColorMode: () => {
                    setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
                },
            }),
            [],
        );
        const theme = React.useMemo(
            () =>
                createTheme({
                    palette: {
                        mode,
                        primary: {
                            main: '#556cd6',
                            dark: '#333'
                        },
                        secondary: {
                            main: '#19857b',
                            dark: '#19857b',
                        },
                        error: {
                            main: red.A400,
                        },
                    },
                }),
            [mode],
        );
        return (
            <React.Fragment>
                <ColorModeContext.Provider value={colorMode}>
                    <ThemeProvider theme={theme}>
                        <CssBaseline />
                        <Component {...props} />
                    </ThemeProvider>
                </ColorModeContext.Provider>
            </React.Fragment>
        )
    };
}

export default makeTheme;
