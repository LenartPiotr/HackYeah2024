import './summary.scss';
import { Settings, SummaryType } from '../../types';
import { categoryMap } from '../../constans';
import SummaryValue from '../SummaryValue/SummaryValue';

const Summary = ({ settings, responses, summaryToggle }: SummaryProps) => {
    const categories = new Set(responses.map((summary: SummaryType) => summary.category));

    const sortedCategories = Array.from(categories).sort((a, b) => {
        return a.localeCompare(b);
    });

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

    const summaryElements = [...sortedCategories].map((category: string) => {
        
        const categoryData = responses
            .filter((summary: SummaryType) => summary.category === category)
            .map((summary: SummaryType) => (
                <SummaryValue
                    type={summary.type}
                    value={summary.value}
                    category={summary.category}
                    language={settings.language}
                />
            ))

        return (
            <div className='summary-category'>
                <h3 className='category-header'>{categoryMap[category as keyof typeof categoryMap][settings.language]}</h3>
                <div className='category-data'>
                    {...categoryData}
                </div>
            </div>
        )
    });

    return (
        <div className={`main-summary ${summaryToggle && 'active'}`}>
            {
                responses.length === 0 ? (
                    <h2 className='summary-title'>
                        {messages['empty-summary-title'][settings.language]}
                    </h2>
                ) : (
                    <>
                        <h2 className='summary-title'>
                            {messages['summary-title'][settings.language]}
                        </h2>
                        {summaryElements}
                        <button className='summary-accept' onClick={handleXml}>
                            {messages['accept-button'][settings.language]}
                        </button>
                    </>
                )
            }
        </div>
    )
};

const messages = {
    'summary-title': {
        'polish': 'Podsumowanie',
        'english': 'Summary',
        'ukrainian': 'Резюме'
    },
    'accept-button': {
        'polish': 'Akceptuj i zapisz',
        'english': 'Confirm and save',
        'ukrainian': 'Підтвердити та зберегти'
    },
    'empty-summary-title': {
        'polish': 'Nie znaleziono żadnych pól formularza',
        'english': 'No form fields found',
        'ukrainian': 'Поля форми не знайдено'
    }
}

type SummaryProps = {
    settings: Settings,
    responses: SummaryType[],
    summaryToggle: boolean,
};

export default Summary;