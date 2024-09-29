import './summary.scss';
import { Settings, SummaryType } from '../../types';
import { categoryMap } from '../../constans';
import SummaryValue from '../SummaryValue/SummaryValue';

const Summary = ({ settings, responses, summaryToggle }: SummaryProps) => {
    const categories = new Set(responses.map((summary: SummaryType) => summary.category));

    const summaryElements = [...categories].map((category: string) => {
        
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
            <h2 className='summary-title'>{messages['summary-title'][settings.language]}</h2>
            {...summaryElements}
            <button className='summary-accept'>{messages['accept-button'][settings.language]}</button>
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
    }
}

type SummaryProps = {
    settings: Settings,
    responses: SummaryType[],
    summaryToggle: boolean,
};

export default Summary;