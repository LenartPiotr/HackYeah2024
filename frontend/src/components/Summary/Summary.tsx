import './summary.scss';
import { Settings, SummaryType } from '../../types';
import { categoryMap, typeMap } from '../../constans';
import { FaRegEdit } from "react-icons/fa";

const Summary = ({ settings, responses }: SummaryProps) => {
    const categories = new Set(responses.map((summary: SummaryType) => summary.category));

    const summaryElements = [...categories].map((category: string) => {
        
        const categoryData = responses
            .filter((summary: SummaryType) => summary.category === category)
            .map((summary: SummaryType) => (
                <div className='category-response-wrapper'>
                    <div className='category-response-block'>
                        <div className='category-type'>{typeMap[summary.type as keyof typeof typeMap][settings.language]}</div>
                        <div className='category-response'>{summary.value}</div>
                    </div>
                    <div className='edit-response-button'>
                        <FaRegEdit 
                            size="20px"
                        />
                        {messages['edit'][settings.language]}
                    </div>
                </div>
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
        <div className='main-summary'>
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
    'edit': {
        'polish': 'Edytuj',
        'english': 'Edit',
        'ukrainian': 'Редагувати',
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
};

export default Summary;