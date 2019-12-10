import {makeStyles} from '@material-ui/styles';
import {Dimensions} from './Components/Dimensions';

//Funktio tyyli moduuli
export function allstyles() {
    
    const dimensions = Dimensions();

    const apph = makeStyles({
        root: {
            height: 60,
            justifyContent: 'center',
            alignItems: 'center',
            backgroundColor: '#388e3c',
        }
    })
    
    const modal = makeStyles({
        root: {
            height: dimensions.height<=800 ? dimensions.height/1.5 : dimensions.height/2,
            width: dimensions.width<=1200 ? dimensions.width/1.5 : dimensions.width/2,
            justifyContent: 'center',
            alignItems: 'center',
        },
    })
    
    const paper = makeStyles({
        root: {
            width: dimensions.width, 
            justifyContent: 'center',
            alignItems: 'center',
            alignContent: 'center'
        }
    })
    
    const mpaper = makeStyles({
        root: {
            height: 300,
            width: 600,
            margin: 5,
            border: 1, 
            borderColor: '#b6b6b6',
        }
    })
    
    const table = makeStyles({
        root: {
            width: dimensions.width/4
        }
    })
    
    const mtable = makeStyles({
        root: {
            height: 300,
            width: 600
        }
    })
        
    const thead = makeStyles({
        root: {
            height: 30,
            width: dimensions.width/4,
            backgroundColor: '#388e3c'
        }
    })

    const mthead = makeStyles({
        root: {
            height: 30,
            backgroundColor: '#388e3c'
        }
    })

    const trow = makeStyles({
        root: {

        }
    })
    
    const tcell = makeStyles({
        root: {
            height: 30,
            width: 80,
            justifyContent: 'center',
            alignItems: 'center'
        }
    })
    
    const mtcell = makeStyles({
        root: {
            height: 60,
            width: 180,
            justifyContent: 'center',
            alignItems: 'center'
        }
    })
    
    const button = makeStyles({
        root: {
            width: 100,
            height: 30,
            backgroundColor: '#ffc107',
            justifyContent: 'center',
            alignItems: 'center'
        }
    })
    
    const icon = makeStyles({
        root: {
            color: '#ffc107',
            fontSize: 32
        }
    })
    
    const plabel = makeStyles({
        root: {
            height: 30,
            width: 65
        }
    })
    
    const piker = makeStyles({
        root: {
            height: 30,
            width: 60
        }
    })
        
    const ifield = makeStyles({
        root: {
            height: 30,
            width: 160,
            border: 1, 
            borderColor: '#b6b6b6',
        }
    })
    
    const txth = makeStyles({
        root: {
            color: '#fff',
            fontFamily: 'Roboto',
            fontSize: 20,
        }
    })
    
    const txt = makeStyles({
        root: {
            color: '#fff',
            fontFamily: 'Roboto',
            fontSize: 18,
        }
    })

    return(
        [apph(), paper(), modal(), mpaper(), table(), mtable(), thead(), mthead(), trow(), tcell(),
            mtcell(), button(), icon(), plabel(), piker(), ifield(), txth(), txt()]
    );
}  