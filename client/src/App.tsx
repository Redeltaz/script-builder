import './App.scss';
import { Overlay } from './component/Overlay/Overlay';
import 'rsuite/dist/rsuite.min.css';
import { Button } from 'rsuite';

function App() {
  return (
    <div className="App">
      <Overlay>
        <Button>Hello World</Button>
      </Overlay>

    </div>
  );
}

export default App;
