import React, {useEffect, useState} from 'react';
import {Typography, AppBar, Paper, TableRow, Table, TableHead, TableCell,
  TableBody, Button} from '@material-ui/core';
import {allstyles} from './styles';
import './App.css'
import {Cmodal} from './Components/Cmodal';

export default function App() {

  const [rates, setRates] = useState({});
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/kurssit');
        const json = await res.json();
        setRates(json);
      } catch (error) {
        console.log("error", error);
      }
    }
    fetchData();
    return () => {}
  }, []);

  const handleClose = () => {
    setOpen(false)
  }

  const handleOpen = () => {
    setOpen(true);
  }

  //Tyyli moduulin alustus
  const jss = allstyles();

  return (
    <div className="root">
      <AppBar position='static' classes={{root: jss[0].root}}>
          <Typography variant="h4">Valuutat</Typography>
        </AppBar>
          <Paper classes={{root: jss[1].root}}>
              <Table classes={{root: jss[2].root}}>
                <TableHead classes={{root: jss[6].root}}>
                  <TableRow>
                    <TableCell>
                      <Typography classes={{root: jss[16].root}}>Nimi</Typography>
                    </TableCell>
                    <TableCell>
                      <Typography classes={{root: jss[16].root}}>Kurssi</Typography>
                    </TableCell>
                    <TableCell>
                    </TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {rates.map(item => (
                    <TableRow key={item.id}>
                      <TableCell classes={{root: jss[9].root}}>
                        <Typography>{item.name}</Typography>
                      </TableCell>
                      <TableCell classes={{root: jss[9].root}}>
                        <Typography>{item.rate}</Typography>
                      </TableCell>
                      <TableCell classes={{root: jss[9].root}}>
                        <Button classes={{root: jss[11].root}} onClick={handleOpen}>
                          <Typography classes={{root: jss[17].root}}>Muunna</Typography>
                        </Button>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Paper>
            <Cmodal 
              all={rates}
              value={open}
              quit={handleClose}
            />
    </div>
  );
}