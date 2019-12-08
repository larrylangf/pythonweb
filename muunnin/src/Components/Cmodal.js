import React, {useState} from 'react';
import {Modal, Table, TableBody, TableHead, TableRow, TableCell, Typography, TextField, MenuItem, Paper, 
  Button} from "@material-ui/core";
import {Close, DragHandle} from '@material-ui/icons';
import {allstyles} from '../styles';
import '../App.css'
//Oma moduuli joka näyttää sisältöä uudessa ikkunassa ilman navigointia
export function Cmodal(props) {

    const [currency, setCurrency] = useState();
    const [convert, setConvert] = useState("EUR");
    const [amount, setAmount] = useState(0);
    const [result, setResult] = useState(0);
    
    const calculate = () => {
      let mapcs = {};
      props.all.map(i => {
        if (i.name === currency) {
          mapcs.curr = i.rate;
        }
        if (i.name === convert) {
          mapcs.conr = i.rate;
        }
      })
        if(currency !== "EUR" && convert === "EUR") {
            setResult((amount / mapcs.curr).toFixed(2));
        }
        else if (currency === "EUR" & convert !== "EUR") {
            setResult((amount * mapcs.conr).toFixed(2));
        }
        else if(mapcs.curr<mapcs.conr) {
          let rate = (mapcs.curr/mapcs.conr);
          setResult((amount * rate).toFixed(2));
        }
        else if (currency === "EUR" & convert === "EUR") {
          setResult(amount);
        }
        else {
          let rate = (mapcs.conr/mapcs.curr);
          setResult((amount * rate).toFixed(2));
        }
      }  

    //Tyyli moduulin alustus
    const jss = allstyles();

    return(
     <div className="root">
      <Modal classes={{root: jss[2].root}} open={props.value}>
       <Paper classes={{root: jss[3].root}}>
         <Table classes={{root: jss[5].root}}>
          <TableHead classes={{root: jss[7].root}}>
            <TableRow>
              <TableCell classes={{root: jss[10].root}}>
                <Button onClick={props.quit}>
                  <Typography classes={{root: jss[16].root}}>Sulje</Typography>
                  <Close classes={{root: jss[12].root}} />
                </Button>
              </TableCell>
              <TableCell classes={{root: jss[10].root}}>
              </TableCell>
              <TableCell classes={{root: jss[10].root}}>
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell classes={{root: jss[10].root}}>
                <TextField
                    classes={{root: jss[13].root}}
                    select
                    label="Mistä:"
                    value={currency}
                    onChange={(e) => setCurrency(e.target.value)}
                >
                  {props.all.map(item => (
                      <MenuItem classes={{root: jss[14].root}} key={item.id} value={item.name}>
                        {item.name}
                      </MenuItem>
                  ))}
                </TextField>
              </TableCell>
              <TableCell classes={{root: jss[10].root}}>
                <TextField
                    classes={{root: jss[13].root}}
                    select
                    label="Mihin:"
                    value={convert}
                    onChange={(e) => setConvert(e.target.value)}
                >
                  {props.all.map(item => (
                    <MenuItem classes={{root: jss[14].root}} key={item.id} value={item.name}>
                      {item.name}
                    </MenuItem>
                  ))}
                </TextField>
              </TableCell>
            </TableRow>
            <TableRow>
              <TableCell classes={{root: jss[10].root}}>
                <TextField
                  classes={{root: jss[15].root}}
                  label='Määrä:'
                  inputMode='decimal'
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                />
              </TableCell>
              <TableCell classes={{root: jss[10].root}}>
                <DragHandle classes={{root: jss[12].root}} />
              </TableCell>
              <TableCell classes={{root: jss[10].root}}>
                <Typography>Tulos:</Typography>
                  <Typography>{result}</Typography>
              </TableCell>
            </TableRow>
            <TableRow>
              <TableCell>
                <Button classes={{root: jss[11].root}} onClick={calculate}>
                  <Typography classes={{root: jss[17].root}}>Laske</Typography>
                </Button>
              </TableCell>
            </TableRow>
          </TableBody>
         </Table>
       </Paper>
      </Modal>
     </div>
    )
}