import axios from 'axios';
import { useQuery } from 'react-query';

type RESTClientType<T> = {
    data: T;
    error: unknown;
    isFetching: boolean;
    isLoading: boolean;
    refetch: () => void;
};

export const useRestClient = <T>(
    dataType: string[],
    url: string,
    payload: Record<string, unknown>,
    enable: boolean
): RESTClientType<T> => {
    const { data, error, isFetching, isLoading, refetch } = useQuery(
        dataType,
        () => axios.post(url, payload).then((res) => res.data.result),
        {
            enabled: enable
        },
    );

    return {
        data,
        error,
        isFetching,
        isLoading,
        refetch
    };
};
