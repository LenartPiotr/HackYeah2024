import classNames from 'classnames';
import PolishFlag from '../../assets/poland-flag.jpg';
import UkFlag from '../../assets/uk-flag.jpg';
import UkraineFlag from '../../assets/ukraine-flag.png';
import { Settings } from '../../types';
import './header.scss';
import { Languages } from '../../enums';
import { CiImport, CiExport } from "react-icons/ci";

const Header = ({ settings, changeLanguage }: HeaderProps) => {

    const handleXml = () => {
        const d = new Date();
        let [date, time] = d.toLocaleString().split(", ");
        date = date.split(".").reverse().join("_");
        time = time.split(":").join("_");
          
        fetch("http://127.0.0.1:8000/xml")
            .then(res => res.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `formularz_${date}_${time}.xml`;
                document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
                a.click();    
                a.remove();  //afterwards we remove the element again  
            });
    };

    return (
        <header className='header-main'>
            <div className='form-info'>
                <h2>PCC-3</h2>
                <p>{messages['form-info-subtitle'][settings.language]}</p>
            </div>
            <div className='settings-panel'>
                <div className='languages'>
                    <p className='language-title'>{messages['language-title'][settings.language]}</p>
                    <div className="flags">
                        <img 
                            src={PolishFlag} 
                            alt='Polish flag'
                            className={classNames({
                                'active': settings.language === 'polish'
                            })}
                            onClick={() => changeLanguage(Languages.polish)}
                        />
                        <img 
                            src={UkFlag} 
                            alt='UK flag'
                            className={classNames({
                                'active': settings.language === 'english'
                            })}
                            onClick={() => changeLanguage(Languages.english)}
                        />
                        <img 
                            src={UkraineFlag} 
                            alt='Ukrainian flag'
                            className={classNames({
                                'active': settings.language === 'ukrainian'
                            })}
                            onClick={() => changeLanguage(Languages.ukrainian)}
                        />
                    </div>
                </div>
                <div className='export-functions'>
                    <div className='function' onClick={handleXml}>{messages['generate-xml'][settings.language]}<CiExport size="25px" /></div>
                </div>
            </div>
        </header>
    )
};

const messages = {
    'form-info-subtitle': {
        'polish': 'Deklaracja w sprawie podatku od czynności cywilnoprawnych',
        'english': 'Statement regarding tax on civil law transactions',
        'ukrainian': 'Декларація з податку на цивільно-правові операції'
    },
    'language-title': {
        'polish': 'Język panelu',
        'english': 'Language panel',
        'ukrainian': 'Мова панелі'
    },
    'generate-xml': {
        'polish': 'Wygeneruj plik XML',
        'english': 'Generate XML file',
        'ukrainian': 'Згенеруйте XML-файл'
    }
};

type HeaderProps = {
    settings: Settings,
    changeLanguage: (type: Languages) => void,
};

export default Header;